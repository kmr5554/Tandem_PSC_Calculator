


def main(Tcell, Egap):
    os.chdir('./')
    Tandem_PSC_Calculator
import os

    os.chdir('./')
    

import os
import numpy as np
import scipy.constants as constants
import matplotlib.pyplot as plt
import pandas as pd

%matplotlib inline

module_dir = os.getcwd()+os.sep

mode=['AMZ.CSV' ,'ASTMG173.csv']
spectrumS = np.loadtxt(module_dir + mode[0], delimiter=',', skiprows=1)
spectrumE = np.loadtxt(module_dir + mode[1], delimiter=',', skiprows=1)

pd_S = pd.DataFrame(spectrumS, columns = ['Wavelength(nm)', 'Irradiance'])
print('\nAMZ.CSV File Contents\n\n',pd_S[:5])
c = constants.value('speed of light in vacuum')
h = constants.value('Planck constant')
e = constants.value('elementary charge')
k = constants.value('Boltzmann constant')

Tcell = 273  # Temperature (kelvin)
Egap = 1.6  # electron volts (Default : silicon 1.1eV)

    E = h * c / converted[:, 0]
    d_lambda_d_E = h * c / E**2
    converted[:, 1] = converted[:, 1] * d_lambda_d_E * e / E
    converted[:, 0] = E / e
    return converted


original_irradianceS = np.trapz(spectrumS[:, 1], spectrumS[:, 0])
original_irradianceE = np.trapz(spectrumE[:, 1], spectrumE[:, 0])

print('Total spectrum AM0 irriadiance   : {:.5f} W/m^2'.format(original_irradianceS))
print('Total spectrum AM2.5 irriadiance : {:.5f} W/m^2'.format(original_irradianceE))

photon_spectrumS = convert_spectrum(spectrumS)
photon_spectrumE = convert_spectrum(spectrumE)
plot_spectra(spectrumS, spectrumE, photon_spectrumS, photon_spectrumE)

photon_irradianceS = np.trapz(photon_spectrumS[::-1, 1] * photon_spectrumS[::-1, 0],
                          photon_spectrumS[::-1, 0]) * e
photon_irradianceE = np.trapz(photon_spectrumE[::-1, 1] * photon_spectrumE[::-1, 0],
                          photon_spectrumE[::-1, 0]) * e

print('If everything went okay this should be pretty close to the number from before...')
print('Space : Original {:.5f} W/m^2\t-->>  Converted {:.5f} W/m^2'
      .format(original_irradianceS, photon_irradianceS))
print('Earth : Original {:.5f} W/m^2\t-->>  Converted {:.5f} W/m^2'
      .format(original_irradianceE, photon_irradianceE))


photons_above_bandgap_plot(Egap,photon_spectrumS,photon_spectrumE)






    plot_phonon(ax2, egap, temperature, spectrum1, label1, voc, '$V_{OC}$ (V)')
    plot_phonon(ax2, egap, temperature, spectrum2, label2, voc, '$V_{OC}$ (V)')
    ax2.set_title('Ideal open-circuit voltage')
    ax2.set_xlim((np.maximum(egap-0.5,0), egap+0.5))
    ax2.set_ylim((np.maximum(egap-0.5,0), egap+0.5))
    plt.show()
print('At space,')
print('A material with a bandgap of %.2f will have an:' % Egap)
print('Ideal short circuit current: ', jsc(Egap, Tcell, photon_spectrumS), 'A/m^2')
print('Ideal open circuit  voltage: ', voc(Egap, Tcell, photon_spectrumS), 'V')
print('\n')
print('At Earth,')
print('A material with a bandgap of %.2f will have an:' % Egap)
print('Ideal short circuit current: ', jsc(Egap, Tcell, photon_spectrumE), 'A/m^2')
print('Ideal open circuit  voltage: ', voc(Egap, Tcell, photon_spectrumE), 'V')
print('\n\n')

ideal_plots(Egap, Tcell, photon_spectrumS, photon_spectrumE, 'Space', 'Earth')

    ax.plot(v, i, label=f'I - V curve')
    ax2 = ax.twinx()
    ax2.plot(v, p, color='orange', label=f'P - V curve')
    ax.set_xlabel('Voltage (V)')
    ax.set_ylabel('Current density $J$ ($Am^{-2}$)')
    ax2.set_ylabel('Power generated ($W$)')
    ax.legend(loc=3, fontsize=10)
    ax2.legend(loc=4, fontsize=10)


plot_iv_curves(Egap, Tcell, [photon_spectrumS, photon_spectrumE], ['Space', 'Earth'])




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

sq_limit_plot(1.6, Tcell, photon_spectrumS, 'Space')
sq_limit_plot(1.6, Tcell, photon_spectrumE, 'Earth')
Egap_min = 0.5 #eV
Egap_max = 3.0



    idx = np.unravel_index(np.argmax(tandemfunc_eff, axis=None), tandemfunc_eff.shape)
    plt.plot(bottom_Egap[idx[1]], top_Egap[idx[0]], 'ro')
    plt.plot(1.38, 2.1, 'bo')
    plt.text(bottom_Egap[idx[1]]-0.1, top_Egap[idx[0]]+0.1, '{:.3}'.format(tandemfunc_eff[idx]))
    plt.show()
    print("Max Efficiency : {:.3f} \nOptimized Bot Cell Bandgap : {:.3f}eV \nOptimized Top Cell Bandgap : {:.3f}eV"\
        .format(tandemfunc_eff[idx],bottom_Egap[idx[1]],top_Egap[idx[0]]))

bottom_Egap, top_Egap, tandemfunc_eff = tandem_max_eff(Tcell, photon_spectrumS, Egap_min=0.5, Egap_max=3.5, linespace=100)
plot_tandem_func(bottom_Egap, top_Egap, tandemfunc_eff)

bottom_Egap, top_Egap, tandemfunc_eff = tandem_max_eff(Tcell, photon_spectrumE, Egap_min=0.5, Egap_max=3.5, linespace=100)
plot_tandem_func(bottom_Egap, top_Egap, tandemfunc_eff)

