import numpy as np

a = np.array([[1,2,3,4],[4,5,6,5]], dtype = 'int32')
print(a)
print()
print(a.ndim)
print(a.shape)
b = a.reshape(4,2)
# print(b)
# print(b.dtype)
# print(a.nbytes)
# print(a.itemsize)

#get a specific row
print(a[0,:])

#get a specific column
print(a[:, 0])

# print(b[2,1])