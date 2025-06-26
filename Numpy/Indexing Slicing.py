import numpy as np

#Indexing

# arr = np.array([1,2,3,4])

# print(arr[0])

# print(arr[2] + arr[0])


#Accessing 2-D Arrays
# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# print('2nd element on 1st row',arr[0,1])

# print('5th element on 2nd row',arr[1,4])

#Accessing 3-D Arrays
# arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# print(arr[0,1,2])

#Negative slicing

# arr = np.array([[1,2,3,4,5,],[6,7,8,9,10]])

# print('Last element from 2nd dimension :', arr[1,-1])

#Slicing

# arr = np.array([1,2,3,4,5,6,7])

# print(arr[1:5])

# print(arr[4:])

# print(arr[:4])

# print(arr[-3:-1])

#STEP

# print(arr[1:5:2])

# print(arr[::2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[1,1:4])

# print(arr[0:2,2])

print(arr[0:2,1:4])