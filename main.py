from utils.runs import *
import sys
import matplotlib

if 'ipykernel' in sys.modules:
    # IPython 환경이라면 inline 백엔드 사용
    matplotlib.use('module://ipykernel.pylab.backend_inline')
    
# Spectrum Comparison
spectrumS, spectrumE = analyze_spectrum()

# Analyze Single PSC
Tcell = float(input("Enter cell temperature (in Kelvin): "))
Egap = float(input("Enter energy gap for single PSC (in eV): "))
calc_single_PSC(Egap, Tcell, spectrumS, spectrumE)

# Calculate Tandem PSC
Egap_min = float(input("Enter minimum bandgap for tandem PSC (in eV): "))
Egap_max = float(input("Enter maximum bandgap for tandem PSC (in eV): "))

bottom_bandgap = float(input("Enter the bottom cell's bandgap you want for tandem (in eV): "))
top_bandgap = float(input("Enter the top cell's bandgap you want for tandem (in eV): "))

calc_tandem_PSC(Tcell, spectrumS, spectrumE, Egap_min, Egap_max, bottom_bandgap, top_bandgap)
