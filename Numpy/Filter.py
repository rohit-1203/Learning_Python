import numpy as np

# arr = np.array([41,42,43,44])
# x = [True,False,True,False]
# newarr = arr[x]
# print(newarr)

# arr = np.array([41,42,43,44])
#
# filter_arr = []
#
# for element in arr:
#     if element >42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)

# arr = np.array([1,2,3,4,5,6,7,8,9,10])

# x = []

# for y in arr:
#     if y % 2 ==0:
#         x.append(True)
#     else:
#         x.append(False)
# z = arr[x]
# print(x)
# print(z)

x = np.array([1,2,3,4,5,6,7,8,9,10])

y = x % 2 == 0
z = x[y]
print(y)
print(z)