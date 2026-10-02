import numpy as np

#----------1 dim----------------
"""a=np.array([10,20,30,40])
print(a)"""

#----------2 dim----------------
"""a=np.array([[1,2,3],[4,5,6]])
print(a)"""

#----------3 dim----------------
"""a=np.array([[[1,2,3]],[[4,5,6]],[[7,8,9]]])
print(a)"""

#-------special array-------------
"""# a=np.zeros((2,3))
# a=np.ones((2,3))
# a=np.eye(4)
# a=np.arange(0,20,3)

# print(a)"""

#----------array attribute---------------
"""a=np.array([[1,2,3],[4,5,6]])

print("shape :", a.shape)
print("ndim :", a.ndim)
print("size :", a.size)
print("dtype :", a.dtype)
print("itemsize :", a.itemsize)"""

#--------------indexing & slicing-------------
#--> 1 dim
"""a = np.array([10,20,30,40,50])

print(a)
print(a[0])
print(a[-1])
print(a[1:4])
print(a[::2])"""

#--> 2 dim 
"""b=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(b)
print(b[0,0])
print(b[1,2])
print(b[:,1])"""

#-----------------reshape and transpose-----------------
"""# a = np.array([[1,2,3],[4,5,6]])
# b = a.reshape(3,2)
# print(b)"""
#-----------
"""#a = np.array([[1,2,3],[4,5,6]])
# print(a.T)
# print(a.flatten())
#print(a.ravel())"""

#---------------BASIC OPERTION--------------------

"""a=np.array([10,12,35])
b=np.array([5,6,7])

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a*2)"""

#-----------------broadcasting-------------------
"""a=np.array([[1,2,3],[4,5,6]])
b=np.array([10,20,30])

print(a)
print(b)
print(a+b)"""

#--------------mathematical functions-------------
"""a=np.array([1,2,3,4])

print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.mean(a))
print(np.sqrt(a))
print(np.sin(a))
print(np.std(a))"""

#--------------aggregation functions-------------
"""a=np.array([[1,2,3],[4,5,6]])

print(a)
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))
print(np.mean(a,axis=0))
print(np.mean(a,axis=1))"""

#--------------logical operations---------------------
"""a = np.array([1,2,3,4,5])

print(a)
print(a < 3)
print(a <= 3)
print((a>2) & (a<5))
print((a==2) | (a==5))"""

#------------conditional selection-------------------
"""a = np.array([10,20,30,40,50])

print(a)
print(np.where(a>25))
print(np.where(a>25,a**2,0))"""

#-------------random module---------------------
"""np.random.seed(0)

print(np.random.rand(5))
print(np.random.randint(1,10,5))
print(np.random.normal(0,1,5))"""

#-----------linear algebra-----------
"""a = np.array([[1,2],[3,4]])

print(a)
print(np.linalg.det(a))
print(np.linalg.inv(a))
print(np.dot(a,a))"""

#----------matrix decompositions----------------
# A=np.array([[1,2],[3,4]])

# U,S,Vt=np.linalg.svd(A)
# print(U)
# print(S)
# print(Vt)

#------------polynomial operations------------
"""p=np.poly1d([1,2,3,4])

print(p)
print(p(2))
roots=np.roots([1,0,-4])
print(roots)"""

#-----------------Statistical Functions----------------
"""a = np.array([1,2,3,4,5,5,6,7,8,9])

print(a)
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Variance:", np.var(a))
print("Std Dev:", np.std(a))"""

#-------------Eigenvalues & Eigenvectors-------------
A = np.array([[2,1],[1,2]])

w,v = np.linalg.eig(A)

print("Eigenvalues:", w)
print("Eigenvectors:\n", v)