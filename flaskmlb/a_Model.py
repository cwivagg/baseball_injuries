import numpy as np

def ModelIt(ip,era,age,fromUser='not default'):
  age *= 365.25
  result = 1 / (1 + np.exp(-0.341026334*ip - 0.0213587214*era + 0.000100886941*age + 0.169989631))
  if fromUser != 'Default':
    return result
  else:
    return 'check your input'