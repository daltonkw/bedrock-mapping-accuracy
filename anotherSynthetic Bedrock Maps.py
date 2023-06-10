# Synthetic Bedrock Maps

# To Do:
# 1. Broaden functions
# 2. Functions -> Classes -> Libraries
# 3. Unit Tests
# 4. How to (best) integrate classification metrics from other libraries?

'''
ORIGINAL DESCRIPTION:
    The functions here are used to build sythetic 'truth' and 'model' grids.
    Bedrock is placed in the landscape as square tors using different
    assumptions for how error is structured in the scene. It also includes
    functions to calculate accuracy and other grid metrics.

FUNCTION DESCRIPTIONS
    1: 'kernel'           Tor centres to bedrock using scipy.signal.convolve2d
    2: 'tor_location'     Iterate over number of tors needed using 'kernel'
    3: 'generate_grid'    Create bedrock map using 'tor_location'
    4: 'model_offset'     Create model grid for translational offset of truth
    5: 'model_rand_err'   Create model grid for random error on truth
    6: 'accuracy_metrics' Calculate TP, FP, FN, TN, F1-score, MCC, nMCC
    7: 'edge_to_area'     Calculate edge to area ratio on given grid

REQUIREMENTS:
    libraries: NumPy, SciPy 

ASSOCIATED MANUSCRIPT:
    Rossi, M.W., in review, Short Communication: Evaluating the accuracy of 
    binary classifiers for geomorphic applications: Earth Surface Dynamics.
'''

import numpy as np
from scipy import signal as sig

'''
scipy.signal.convolve2d(in1, in2, mode='full', boundary='fill', fillvalue=0)
returns: ndarray, A 2-dimensional array containing a subset of the discrete linear convolution of in1 with in2
'''