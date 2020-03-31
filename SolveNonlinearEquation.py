from scipy import poly1d
import numpy as np

a = np.array([1,-2,4.5,-4,0.5])
f = np.poly1d(a)
print(f)
print(f.r)
