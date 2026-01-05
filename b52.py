import numpy as np

arr = np.array([10,20,30])

norm = (arr - arr.min())/(arr.max()-arr.min())

print(norm)