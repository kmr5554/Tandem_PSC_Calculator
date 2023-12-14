<p float="left">
  <img src="img/Space.png" width="300" />
  <img src="img/TSC.png" width="300" />
</p>

# :bulb: Shockley-Queisser Limit Calculator 
- Modified Version

This repository contains my modified version of the Shockley-Queisser Limit Calculator, a Jupyter notebook originally designed for calculating the detailed balance limit for the efficiency of a single-junction solar cell. The original concept was published by William Shockley and Hans J. Queisser in 1961.

This project is a collaborative effort between [kmr5554](https://github.com/kmr5554) and [himoon8805](https://github.com/himoon8805)

## :hammer_and_wrench: Modifications and Enhancements

Based on the original Mathematica script by Steve Byrnes, available at [Steve Byrnes's SQ Calculator](link-to-original-calculator), my version of this notebook includes several modifications and enhancements, aiming to expand its functionality and improve user experience. Key modifications include:

- :rocket: Streamlined data processing algorithms.
- :art: Enhanced visualization features using matplotlib.
- :stars: Extended calculations for space and tandem solar cells.

## :trophy: Original Project Acknowledgment

I would like to acknowledge the original work from which this project is derived. The initial script and methodology were heavily inspired by Steve Byrnes's Mathematica script. The original notebook focused on the ASTM G173 AM1.5 spectrum, and much of the detailed explanations were sourced from Steve's document. For more information on the original work, please refer to [Steve Byrnes's SQ Calculator](link-to-original-calculator).

## :scroll: Data Source Acknowledgment

The spectral data files `AMZ.csv` and `ASTMG173.csv` are sourced from the National Renewable Energy Laboratory (NREL). `AMZ.csv` represents the solar spectrum in space, while `ASTMG173.csv` corresponds to the Earth’s AM1.5 spectrum. These files are crucial for the analysis of solar cell efficiency under different environmental conditions.

## :file_folder: Project Structure

The project is organized as follows:

- `TSC_Efficiency_Analysis.ipynb`: Contains all functions and the complete analysis process.
- `main.py` and the `utils/` directory (`util.py` and `runs.py`): Consist of the core functionality and calculations.
- `Calculator_Demo.ipynb`: Demonstrates how to run the program in a Colab local environment.

## :gear: Local Setup

To use this modified version of the Shockley-Queisser Limit Calculator, ensure you have Jupyter notebook installed.

The project has been tested with the following library versions:

- Numpy version: 1.24.3
- Scipy version: 1.10.1
- Matplotlib version: 3.7.1
- Pandas version: 2.1.3 (Optional)

You can install the required packages using:

```bash
pip install -r requirements.txt
```

## :computer: Usage

To run the notebook:

1. Clone this repository to your local machine.
2. Navigate to the cloned directory.
3. Run `jupyter notebook` to start the Jupyter notebook server.
4. Open the `TSC_Efficiency_Analysis.ipynb` notebook from the server interface.

To run the program in a Colab environment using `Calculator_Demo.ipynb`:

1. Open the `Calculator_Demo.ipynb` file in Google Colab.
2. Follow the instructions within the notebook to execute the analysis.
