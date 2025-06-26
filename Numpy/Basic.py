import numpy as np

# arr = np.array([1,2,3,4,5])

# print(arr)

# print(np.__version__)

#Dimension

#0D

D0 = np.array(42)
print(D0)

#1D

D1 = np.array([1,2,3,4,5])
print(D1)

#2D

D2 = np.array(([1,2,3], [4,5,6]))
print(D2)

#3D

D3 =  np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(D3)

#Check number of dimension

print(D0.ndim)
print(D1.ndim)
print(D2.ndim)
print(D3.ndim)

#Higher Dimensional array

mt = np.array([1, 2, 3, 4], ndmin=5)

print(mt)
print('number of dimensions :', mt .ndim)