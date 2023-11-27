a = 3
print(a)

import matplotlib.pyplot as plt
import numpy as np
from numpy import random as rndm
from random import seed
a = rndm.normal(0, 1, 199)
print(a)
np.mean(a)

rndm.seed(42)
n_replicates = 200
result = np.zeros(n_replicates)
for i in range(n_replicates):
  draw = rndm.normal(0, 1, 100)
  result[i] = np.mean(draw)
  
np.mean(result)
  
  
