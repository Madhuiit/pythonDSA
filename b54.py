import numpy as np

arr = np.array([-2,5,-7.8])

arr[arr<0] = 0

print(arr)