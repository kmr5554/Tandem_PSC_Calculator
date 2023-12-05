## Shockley-Queisser Limit Calculator - Modified Version

This repository contains my modified version of the Shockley-Queisser Limit Calculator, a Jupyter notebook originally designed for calculating the detailed balance limit for the efficiency of a single-junction solar cell. The original concept was published by William Shockley and Hans J. Queisser in 1961. This project is a collaborative effort between kmr5554@snu.ac.kr and himoon8805@snu.ac.kr

### Modifications and Enhancements

Based on the original Mathematica script by Steve Byrnes, available at [Steve Byrnes's SQ Calculator](http://sjbyrnes.com/sq.pdf), my version of this notebook includes several modifications and enhancements, aiming to expand its functionality and improve user experience. Key modifications include:

- Streamlined data processing algorithms.
- Enhanced visualization features using `matplotlib`.
- Extended calculations for lower irradiances and alternative light sources beyond the sun.

### Original Project Acknowledgment

I would like to acknowledge the original work from which this project is derived. The initial script and methodology were heavily inspired by Steve Byrnes's Mathematica script. The original notebook focused on the ASTM G173 AM1.5 spectrum, and much of the detailed explanations were sourced from Steve's document. For more information on the original work, please refer to [Steve Byrnes's SQ Calculator](http://sjbyrnes.com/sq.pdf).

### Local Setup

To use this modified version of the Shockley-Queisser Limit Calculator, ensure you have Jupyter notebook installed. 

The project has been tested with the following library versions:

* Numpy version: 1.24.3
* Scipy version: 1.10.1
* Matplotlib version: 3.7.1
* Pandas version: 2.1.3 (Optional)

You can install the required packages using:

```bash
pip install -r requirements.txt
```

### Usage

To run the notebook:

1. Clone this repository to your local machine.
2. Navigate to the cloned directory.
3. Run `jupyter notebook` to start the Jupyter notebook server.
4. Open the Shockley-Queisser Limit Calculator notebook from the server interface.
