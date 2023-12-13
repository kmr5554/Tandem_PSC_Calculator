import os
import numpy as np
import scipy.constants as constants
import matplotlib.pyplot as plt
import pandas as pd

c = constants.value('speed of light in vacuum')
h = constants.value('Planck constant')
e = constants.value('elementary charge')
k = constants.value('Boltzmann constant')

def convert_spectrum(spectrum):
    """
    Spectrum input        x: Wavelength (nm),   y: Irradiance (W/m2/nm)
    Converted output      x: Energy (eV),       y: Number of photons (Np/m2/s/dE)
    """
    converted = np.copy(spectrum)
    converted[:, 0] = converted[:, 0] * 1e-9  # wavelength to m
    converted[:, 1] = converted[:, 1] / 1e-9  # irradiance to W/m2/m (from W/m2/nm)
    
    E = h * c / converted[:, 0]
    d_lambda_d_E = h * c / E**2
    converted[:, 1] = converted[:, 1] * d_lambda_d_E * e / E
    converted[:, 0] = E / e
    return converted


def plot_spectrum(ax, spectrum, title, x_label, y_label, label,
                  x_lim=None, y_lim=None, linewidth=1):
    ax.plot(spectrum[:, 0], spectrum[:, 1], label=label, linewidth=linewidth)
    ax.set_xlim(x_lim)
    ax.set_ylim(y_lim)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend()
    ax.set_title(title)
    
    
def plot_spectra(spectrumS, spectrumE, convertedS, convertedE):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    plot_spectrum(ax1, spectrumS, 'Spectrum Irradiance', 'Wavelength (nm)',
                  'Spectral Irradiance ($Wm^{-2}nm^{-1}$)', 'Space', (0,3000))
    plot_spectrum(ax1, spectrumE, 'Spectrum Irradiance', 'Wavelength (nm)',
                  'Spectral Irradiance ($Wm^{-2}nm^{-1}$)', 'Earth', (0,3000))
    plot_spectrum(ax2, convertedS, 'Converted spectrum', 'Energy (eV)',
                  '# Photons $m^{-2}s^{-1}dE$', 'Space', (0,5))
    plot_spectrum(ax2, convertedE, 'Converted spectrum', 'Energy (eV)',
                  '# Photons $m^{-2}s^{-1}dE$', 'Earth', (0,5), linewidth=0.3)
    plt.show()
    
    
def photons_above_bandgap(egap, spectrum):
    """Counts number of photons above given bandgap"""
    indexes = np.where(spectrum[:, 0] > egap)
    y = spectrum[indexes, 1][0]
    x = spectrum[indexes, 0][0]
    return np.trapz(y[::-1], x[::-1])


def photons_above_bandgap_plot(egap, spectrum1, spectrum2):
    #Plot bandgap vs # of photons above bandgap
    spectra=[spectrum1, spectrum2]
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    copied_spectra = [np.copy(spectrum1), np.copy(spectrum2)]
    names = ['Space','Earth']
    for i, ax in enumerate(axes):
        spectrum = copied_spectra[i]
        for row in spectrum:
            row[1] = photons_above_bandgap(row[0], spectra[i])
        ax.plot(spectrum[:, 0], spectrum[:, 1])
        p_above_egap = photons_above_bandgap(egap, spectra[i])
        ax.plot([egap], [p_above_egap], 'ro')
        ax.text(egap+0.05, p_above_egap, '{}eV, {:.2}'.format(egap, p_above_egap))
        ax.set_xlabel('$E_{gap}$ (eV)')
        ax.set_ylabel('# Photons $m^{-2}s^{-1}$')
        ax.set_title(f'# of above-Eg photons for {names[i]}',pad=20)
    plt.show()
    
    
def rr0(egap, Temperature,spectrum):
    k_eV = k / e
    h_eV = h / e
    const = (2 * np.pi) / (c**2 * h_eV**3)
    E = spectrum[::-1, ]  # in increasing order of bandgap energy
    egap_index = np.where(E[:, 0] >= egap)
    numerator = E[:, 0]**2
    exponential_in = E[:, 0] / (k_eV * Temperature)
    denominator = np.exp(exponential_in) - 1
    integrand = numerator / denominator
    integral = np.trapz(integrand[egap_index], E[egap_index, 0])
    result = const * integral
    
    if result[0] <= 0:
        result[0] = 1e-20
        
    return result[0]


def recomb_rate(egap, Temperature, spectrum, voltage):
    return e * rr0(egap, Temperature, spectrum) * np.exp(e * voltage / (k * Temperature))


def current_density(egap, Temperature, spectrum, voltage):
    return e * (photons_above_bandgap(egap, spectrum) - rr0(egap, Temperature, spectrum)
                * np.exp(e * voltage / (k * Temperature)))
    
    
def jsc(egap, Temperature, spectrum):
    return current_density(egap, Temperature, spectrum, 0)


def voc(egap, Temperature, spectrum):
    photons_rr0 = photons_above_bandgap(egap, spectrum)/ rr0(egap, Temperature, spectrum)
    if photons_rr0 <=0:
        photons_rr0 = 1e-20
    return (k * Temperature / e) * np.log(photons_rr0)


def plot_phonon(ax, egap, temperature, spectrum, label, calc_func, y_label):
    a = np.copy(spectrum)
    for row in a:
        row[1] = calc_func(row[0], temperature, spectrum)
    ax.plot(a[:, 0], a[:, 1], label=label)
    p_above_egap = calc_func(egap, temperature, spectrum)
    ax.plot([egap], [p_above_egap], 'ro')
    ax.text(egap + 0.05, p_above_egap, '{}eV, {:.4}'.format(egap, p_above_egap))
    ax.set_xlabel('$E_{gap}$ (eV)')
    ax.set_ylabel(y_label)
    ax.legend()
    ax.set_xlim((egap-1, egap+1))
    
    
def ideal_plots(egap, temperature, spectrum1, spectrum2, label1, label2):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    plot_phonon(ax1, egap, temperature, spectrum1, label1, jsc, '$J_{SC}$ $Am^{-2}$')
    plot_phonon(ax1, egap, temperature, spectrum2, label2, jsc, '$J_{SC}$ $Am^{-2}$')
    ax1.set_title('Ideal short-circuit current')
    ax1.set_xlim((np.maximum(egap-0.5,0), egap+0.5))
    ax1.set_ylim(bottom=0)
    plot_phonon(ax2, egap, temperature, spectrum1, label1, voc, '$V_{OC}$ (V)')
    plot_phonon(ax2, egap, temperature, spectrum2, label2, voc, '$V_{OC}$ (V)')
    ax2.set_title('Ideal open-circuit voltage')
    ax2.set_xlim((np.maximum(egap-0.5,0), egap+0.5))
    ax2.set_ylim((np.maximum(egap-0.5,0), egap+0.5))
    plt.show()
    
    
def plot_iv_curve(ax, egap, temperature, spectrum, label):
    v_open = voc(egap, temperature, spectrum)
    v = np.linspace(0, v_open, 100)
    i = current_density(egap, temperature, spectrum, v)
    p = v * i
    
    ax.plot(v, i, label=f'I - V curve')
    ax2 = ax.twinx()
    ax2.plot(v, p, color='orange', label=f'P - V curve')
    ax.set_xlabel('Voltage (V)')
    ax.set_ylabel('Current density $J$ ($Am^{-2}$)')
    ax2.set_ylabel('Power generated ($W$)')
    ax.legend(loc=3, fontsize=10)
    ax2.legend(loc=4, fontsize=10)    
    
    
def plot_iv_curves(egap, temperature, spectra, labels):
    fig, axes = plt.subplots(1, len(spectra), figsize=(10, 4))
    for ax, spectrum, label in zip(axes, spectra, labels):
        plot_iv_curve(ax, egap, temperature, spectrum, label)
        plt.title(label)
    plt.subplots_adjust(wspace=0.5)
    plt.show()
    
    
def v_at_mpp(egap, temperature, spectrum):
    v_open = voc(egap, temperature, spectrum)
    v = np.linspace(0, v_open)
    index = np.where(v * current_density(egap, temperature, spectrum, v)
                     == max(v * current_density(egap, temperature, spectrum, v)))
    return v[index][0]


def max_power(egap, temperature, spectrum):
    v_open = voc(egap, temperature, spectrum)
    v = np.linspace(0, v_open)
    index = np.where(v * current_density(egap, temperature, spectrum, v)
                     == max(v * current_density(egap, temperature, spectrum, v)))
    return max(v * current_density(egap, temperature, spectrum, v))


def j_at_mpp(egap, temperature, spectrum):
    return max_power(egap, temperature, spectrum) / v_at_mpp(egap, temperature, spectrum)


def max_eff(egap, temperature, spectrum):
    irradiance =  np.trapz(spectrum[::-1, 1] * e * spectrum[::-1, 0], spectrum[::-1, 0])
    return max_power(egap, temperature, spectrum) / irradiance


def sq_limit_plot(egap, temperature, spectrum, label):
    a = np.copy(spectrum)
    for row in a[2:]:
        row[1] = max_eff(row[0],  temperature, spectrum)
    plt.plot(a[2:, 0], a[2:, 1])
    
    opt_Eg_index = np.argmax(a[2:, 1])
    opt_Eg=spectrum[opt_Eg_index,0]
    max_Eff=max_eff(opt_Eg, temperature, spectrum)

    print('For {}, Optimal Bandgap : {:.4f} , Max Efficiency : {:.4f}%'.format(label, opt_Eg, max_Eff*100))

    print('++ Ideal Efficiency for Bandgap {:.2f} eV : {:.4}% \n'.format(egap, max_eff(egap, temperature, spectrum)*100))

    p_above_egap = max_eff(egap, temperature, spectrum)
    plt.plot([egap], [p_above_egap], 'ro')
    plt.text(egap+0.05, p_above_egap, '{}eV : {:.2f}% ({})'.format(egap, p_above_egap*100, label))
    plt.xlim((0.2,4))

    plt.xlabel('$E_{gap}$ (eV)')
    plt.ylabel('Max efficiency')
    plt.title('SQ Limit')
    plt.show()
    
    
def tandem_max_power(top_Egap, bottom_Egap, temperature, spectrum):
    if bottom_Egap >= top_Egap:
        result = 0  #top_Egap must be bigger than bottom_Egap
    else:
        top_max_power = max_power(top_Egap, temperature, spectrum)
        indexes = np.where(spectrum[:, 0] < top_Egap)
        bottom_spectrum = spectrum[indexes]
        bottom_max_power = max_power(bottom_Egap, temperature, bottom_spectrum)
        result = top_max_power + bottom_max_power
    return result


def tandem_max_eff(temperature, spectrum, Egap_min, Egap_max, linespace):
    bottom_range = np.linspace(Egap_min, Egap_max-0.01, linespace)
    top_range = np.linspace(Egap_min+0.01, Egap_max, linespace)
    # bottom_Egap, top_Egap = np.meshgrid(x, y)
    tandemfunc = np.zeros((linespace, linespace))
    for i in range(linespace):
        for j in range(linespace):
            tandemfunc_v= tandem_max_power(top_range[i], bottom_range[j], temperature, spectrum)
            tandemfunc[i, j] = tandemfunc_v
    irradiance = np.trapz(spectrum[::-1, 1] * e * spectrum[::-1, 0], spectrum[::-1, 0])
    tandemfunc_eff = np.nan_to_num(tandemfunc / irradiance)
    
    return bottom_range, top_range, tandemfunc_eff


def plot_tandem_func(bottom_range, top_range, tandemfunc_eff, bottom_Egap, top_Egap ):
    plt.contourf(bottom_range, top_range, tandemfunc_eff, cmap='viridis')  # Filled contour plot
    plt.colorbar()  # Add colorbar
    plt.xlabel('Bottom $E_{gap}$ (eV)')
    plt.ylabel('Top $E_{gap}$ (eV)')
    plt.title('Tandem solar cell Efficiency')
    
    idx = np.unravel_index(np.argmax(tandemfunc_eff, axis=None), tandemfunc_eff.shape)
    
    plt.plot(bottom_range[idx[1]], top_range[idx[0]], 'ro', label='Ideal')
    plt.text(bottom_range[idx[1]] + 0.05, top_range[idx[0]] - 0.05, 
             '{:.3f}'.format(tandemfunc_eff[idx]), color='red')
    
    idx_user = tuple([np.abs(top_range - top_Egap).argmin(), np.abs(bottom_range - bottom_Egap).argmin()])
    
    plt.plot(bottom_range[idx_user[1]], top_range[idx_user[0]], 'bo', label='Yours')
    plt.text(bottom_range[idx_user[1]] + 0.05, top_range[idx_user[0]] - 0.05, 
             '{:.3f}'.format(tandemfunc_eff[idx_user]), color='blue')
    plt.axhline(y=top_range[idx_user[0]], color='blue', linestyle='--')
    plt.axvline(x=bottom_range[idx_user[1]], color='blue', linestyle='--')

    plt.legend()
    plt.show()
    print("Max Efficiency : {:.3f} \nOptimized Bot Cell Bandgap : {:.3f}eV \nOptimized Top Cell Bandgap : {:.3f}eV\n"\
        .format(tandemfunc_eff[idx],bottom_range[idx[1]],top_range[idx[0]]))
    print("User's Tandem Cell Efficiency : {:.3f}\n\n".format(tandemfunc_eff[idx_user]))
