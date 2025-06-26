from difflib import ndiff

import numpy as np

# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print((arr.shape))

arr = np.array([1,2,3,4,5],ndmin=5)

print(arr)
print('Shape of Array is',arr.shape)