from .util import *

#def main(Tcell, Egap, Egap_min, Egap_max):
def analyze_spectrum():
    # Tcell : Temperature (kelvin)
    # Egap : electron volts for single PSC (cf. silicon 1.1eV)
    # Egap_min : minimum electron volts to test for tandem solar cell
    # Egap_max : maximum electron volts to test for tandem solar cell
    
    print(os.getcwd())    

    module_dir = os.getcwd()+os.sep
    
    # AMZ : AM zero condition / ASTMG173 : Earth standard condition
    mode=['AMZ.csv' ,'ASTMG173.csv']
    spectrumS = np.loadtxt(module_dir + mode[0], delimiter=',', skiprows=1)
    spectrumE = np.loadtxt(module_dir + mode[1], delimiter=',', skiprows=1)

    pd_S = pd.DataFrame(spectrumS, columns = ['Wavelength(nm)', 'Irradiance'])
    print('\nAMZ.CSV File Contents\n\n',pd_S[:5])

    original_irradianceS = np.trapz(spectrumS[:, 1], spectrumS[:, 0])
    original_irradianceE = np.trapz(spectrumE[:, 1], spectrumE[:, 0])

    print('\n\nTotal spectrum AM0 irriadiance   : {:.5f} W/m^2'.format(original_irradianceS))
    print('\n\nTotal spectrum AM1.5 irriadiance : {:.5f} W/m^2'.format(original_irradianceE))

    photon_spectrumS = convert_spectrum(spectrumS)
    photon_spectrumE = convert_spectrum(spectrumE)
    plot_spectra(spectrumS, spectrumE, photon_spectrumS, photon_spectrumE)

    photon_irradianceS = np.trapz(photon_spectrumS[::-1, 1] * photon_spectrumS[::-1, 0],
                            photon_spectrumS[::-1, 0]) * e
    photon_irradianceE = np.trapz(photon_spectrumE[::-1, 1] * photon_spectrumE[::-1, 0],
                            photon_spectrumE[::-1, 0]) * e

    print('\n\nIf everything went okay this should be pretty close to the number from before...\n')
    print('Space : Original {:.5f} W/m^2\t-->>  Converted {:.5f} W/m^2'
        .format(original_irradianceS, photon_irradianceS))
    print('Earth : Original {:.5f} W/m^2\t-->>  Converted {:.5f} W/m^2\n\n'
        .format(original_irradianceE, photon_irradianceE))
    
    return photon_spectrumS, photon_spectrumE


def calc_single_PSC(Egap, Tcell, photon_spectrumS, photon_spectrumE):
    photons_above_bandgap_plot(Egap, photon_spectrumS, photon_spectrumE)

    print('\n\nAt space,')
    print('A material with a bandgap of %.2f will have an:' % Egap)
    print('Ideal short circuit current: ', jsc(Egap, Tcell, photon_spectrumS), 'A/m^2')
    print('Ideal open circuit  voltage: ', voc(Egap, Tcell, photon_spectrumS), 'V')
    print('At Earth,')
    print('A material with a bandgap of %.2f will have an:' % Egap)
    print('Ideal short circuit current: ', jsc(Egap, Tcell, photon_spectrumE), 'A/m^2')
    print('Ideal open circuit  voltage: ', voc(Egap, Tcell, photon_spectrumE), 'V')
    print('\n')

    ideal_plots(Egap, Tcell, photon_spectrumS, photon_spectrumE, 'Space', 'Earth')

    plot_iv_curves(Egap, Tcell, [photon_spectrumS, photon_spectrumE], ['Space', 'Earth'])

    sq_limit_plot(Egap, Tcell, photon_spectrumS, 'Space')
    sq_limit_plot(Egap, Tcell, photon_spectrumE, 'Earth')


def calc_tandem_PSC(Tcell, photon_spectrumS, photon_spectrumE, Egap_min, Egap_max, bottom_bandgap, top_bandgap):
    print('\n\n')
    bottom_range, top_range, tandemfunc_eff = tandem_max_eff(Tcell, photon_spectrumS, Egap_min, Egap_max, linespace=100)
    plot_tandem_func(bottom_range, top_range, tandemfunc_eff, bottom_bandgap, top_bandgap)

    bottom_range, top_range, tandemfunc_eff = tandem_max_eff(Tcell, photon_spectrumE, Egap_min, Egap_max, linespace=100)
    plot_tandem_func(bottom_range, top_range, tandemfunc_eff, bottom_bandgap, top_bandgap)

