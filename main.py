
import argparse
from utils.runs import *    

parser = argparse.ArgumentParser(description="Run tandem solar cell efficiency analysis.")
parser.add_argument('--spectrum', default = None, help="Solar Spectrum Data", required=False)
parser.add_argument('--Tcell', type=float, help="Cell temperature in Kelvin", required=True)
parser.add_argument('--Egap', type=float, help="Energy gap for single PSC in eV", required=True)
parser.add_argument('--Egap_min', type=float, help="Minimum bandgap for tandem PSC in eV", required=True)
parser.add_argument('--Egap_max', type=float, help="Maximum bandgap for tandem PSC in eV", required=True)
parser.add_argument('--bottom_bandgap', type=float, help="Bottom cell's bandgap for tandem in eV", required=True)
parser.add_argument('--top_bandgap', type=float, help="Top cell's bandgap for tandem in eV", required=True)

args = parser.parse_args()

# Spectrum Comparison
spectrumS, spectrumE = analyze_spectrum()

# Analyze Single PSC
calc_single_PSC(args.Egap, args.Tcell, spectrumS, spectrumE)

# Calculate Tandem PSC
calc_tandem_PSC(args.Tcell, spectrumS, spectrumE, args.Egap_min, args.Egap_max, args.bottom_bandgap, args.top_bandgap)

#Usage : %run main.py --Tcell=300 --Egap=1.1 --Egap_min=0.5 --Egap_max=2.5 --bottom_bandgap=1.2 --top_bandgap=1.8
