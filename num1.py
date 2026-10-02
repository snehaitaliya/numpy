import numpy as np

# a=np.array([1,2,3,4])
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# a=np.array([[[1,2],[3,4],[5,6],[7,8]]])
# a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

#print(a)


#-----------------ARRAY ATTRIBUTE--------------------

"""
# a=np.array([1,2,3,4])
#a=np.array([[1,2,3],[4,5,6],[7,8,9]])
#a=np.array([[[1,2],[3,4],[5,6],[7,8]]])
# a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

# print(a.shape)"""


#a=np.array([1,2,3,4])
#a=np.array([[1,2,3],[4,5,6],[7,8,9]])
#a=np.array([[[1,2],[3,4],[5,6],[7,8]]])
#a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

#print(a.ndim)

"""
# a=np.array([1,2,3,4])
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# a=np.array([[[1,2],[3,4],[5,6],[7,8]]])
# a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

# print(a.size)"""


#a=np.array([1,2,3,4])
#a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# a=np.array([[[1,2],[3,4],[5,6],[7,8]]])
# a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

#print(a.dtype)

"""
#a=np.array([1,2,3,4])
#a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# a=np.array([[[1,2],[3,4],[5,6],[7,8]]])
# a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

#print(a.itemsize)"""


#-->one dim
#a=np.array([11,26,39,42,55,60,71,87])

#print(a[0])
#print(a[1:6])
#print(a[3:])
#print(a[:4])
#print(a[::2])
#print(a[-4])

#-->two dim
#a=np.array([[1,2,3],[4,5,6],[7,8,9]])

#print(a[2,2])
#print(a[2,1])
#print(a[:,1])
#print(a[2,:])

#-->three dim
# a=np.array([[[1,2,3]],[[4,5,6]],[[7,8,9]]])

# print(a)
#print(a[0,1,0])
#print(a[0,0,1])
#print(a[1,0,0])
#print(a[2,0,2])
#print(a[:,0,1])
#print(a[:,:,1])
#print(a[:,:,0])
#print(a[1,:,:])
#print(a[:,0,:])
#print(a[2,0,:])
#print(a[0,:,1])
#print(a[-2])
#print(a[-1,-1,-1])
#print(a[::-1])            #reverse array


#---------------------------------------------------------
#-->BASIC OPERTION

# a=np.array([10,12,35])
# b=np.array([5,6,7])

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a*2)


#MATHEMATICAL FUNCTION
"""a=np.array([1,9,16])
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.mean(a))
print(np.sqrt(a))
print(np.sin(a))"""


#-->array creation function

# a = np.zeros((2,3))
# a = np.ones((2,3))
# a = np.full((3,2), 5)
# a=np.arange(0,20,3)
# a = np.linspace(0,6,5)
# a = np.eye(4)
# a = np.random.rand(2,3)

# print(a)


#-->reshape and transpose
"""# a = np.array([[1,2,3],[4,5,6]])
# b = a.reshape(3,2)
# print(b)

#a = np.array([[1,2,3],[4,5,6]])
# print(a.T)
# print(a.flatten())
#print(a.ravel())"""


#-->CALCULATION
# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[7,8,9],[10,11,12]])

# print("a + b =\n", a + b)
# print("a * b =\n", a * b)
# print("Sum of all elements:", np.sum(a))
# print("Mean of each column:", np.mean(a, axis=0))

# import numpy as np

n = int(input("Enter dimension: "))
size = 2 ** n
a = np.arange(size)
print("Array:")
print(a)
print("Dimension:", a.ndim)