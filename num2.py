import numpy as np

#-----------universal functions-----------------
"""a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
# print(np.add(a,b))
# print(np.subtract(a,b))
# print(np.multiply(a,b))
# print(np.divide(a,b))
# print(np.power(a,b))
# print(np.sqrt(b))
# print(np.sin(a))
# print(np.cos(a))
# print(np.tan(a))
# print(np.log(a))
# print(np.exp(a))"""

#-----------------broadcasting-------------------
"""a=np.array([[1,2,3],[4,5,6]])
b=np.array([10,20,30])

print(a)
print(b)
print(a+b)"""

#---------aggregation functions------------
"""a=np.array([[1,2,3],[4,5,6]])

# print(a)
# print(np.sum(a))
# print(np.prod(a))
# print(np.mean(a))
# print(np.median(a))
# print(np.std(a))    
# print(np.min(a))
# print(np.max(a))
# print(np.argmin(a))
# print(np.argmax(a))"""

#---------axis operation----------------
"""a=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a)
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))
print(np.mean(a,axis=0))"""

#-----------------sorting-------------------
"""a=np.array([1,3,5,1,2,4,6,8,7,3,2,1])
print(np.sort(a))
print(np.argsort(a))"""

#------------------searching-----------------
"""a=np.array([1,3,5,1,2,4,6,8,7,3,2,1])
print(np.searchsorted(a,5))
print(np.where(a>5))"""

#-----------------counting-------------------
"""a=np.array([1,3,5,1,2,4,6,8,7,3,2,1])
print(np.count_nonzero(a))
print(np.unique(a))
print(np.bincount(a))"""

#-----------------reshape and transpose-----------------

"""a = np.arange(1, 13)
print(a)

b = a.reshape(3,4)
print(b)

print(b.ravel())
print(b.flatten())
print(np.expand_dims(a, axis=0))
print(np.expand_dims(a, axis=1))

x = np.array([[[1,2,3,4]]])

print(np.squeeze(x))
print(np.transpose(b))
print(b.T)
print(np.swapaxes(b, 0, 1))"""

#-----------stacking and splitting-----------------
"""a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a)
print(b)
print(np.hstack((a, b)))
print(np.vstack((a, b)))
print(np.concatenate((a, b)))
print(np.stack((a, b)))"""
#splitting
"""a=np.arange(10)
print(a)
print(np.split(a, 2))
print(np.array_split(a, 3))
print(np.hsplit(a, 2))
print(np.vsplit(a.reshape(2,5), 2))"""

#-------------boolean indexing-----------------
"""a = np.array([10, 20, 30, 40, 50, 60])
print(a)
mask = a > 30
print(mask)
print(a[mask])
print(a%20 == 0)"""

#--------------fancy indexing-----------------
"""a = np.array([10, 20, 30, 40, 50, 60])
print(a)
idx=np.array([0, 2, 4])
print(a[idx])
print(a[[1, 3, 5]])"""

#----------random number generation-----------------
"""np.random.seed(0)
np.random.rand(2,6)
print("randn : \n",np.random.randn(2,3))
print("random : \n",np.random.random((2,2)))
print("randit : \n",np.random.randint(1,10,size=(2,4)))
print("normal : \n",np.random.normal(50,10,5))

a=[10, 20, 30, 40, 50]
print("choice : \n",np.random.choice(a))
print("shuffle : ")
np.random.shuffle(a)
print(a)"""

#--------element wise conditional operations---------
"""a=np.array([10,20,30,40,50])
b=np.where(a>25,'high','low')
c=np.where(a%2==0,a*2,a*3)

print(a)
print(b)
print(c)"""

#-------------------------Matrix Decompositions (np.linalg)-----------------------      
"""A = np.array([[4, 1],[1, 3]])
w,v = np.linalg.eig(A)

print("Eigenvalues:")
print(w)
print("\nEigenvectors:")
print(v)
Output:
Eigenvalues:
[4.61803399 2.38196601]

Eigenvectors:
[[ 0.85065081 -0.52573111]
 [ 0.52573111  0.85065081]

U, S, VT = np.linalg.svd(A)
print("\nU Matrix:")
print(U)
print("\nSingular Values:")
print(S)
print("\nVT Matrix:")
print(VT)
Output:
U Matrix:
[[-0.85065081 -0.52573111]
 [-0.52573111  0.85065081]]

Singular Values:
[4.61803399 2.38196601]

VT Matrix:
[[-0.85065081 -0.52573111]
 [-0.52573111  0.85065081]]

L = np.linalg.cholesky(A)
print("\nCholesky Matrix:")
print(L)
Output:
[[2.         0.        ]
 [0.5        1.6583124 ]]

Q,R = np.linalg.qr(A)
print("\nQ Matrix:")
print(Q)
print("\nR Matrix:")
print(R)
Output:
Q Matrix:
[[-0.9701425  -0.24253563]
 [-0.24253563  0.9701425 ]]

R Matrix:
[[-4.12310563 -1.69774938]
 [ 0.          2.66789188]]"""   
                            
 #---------------------------Advanced Mathematical Functions-----------------
"""a = np.array([-2.7, -1.2, 0.3, 2.6])
print(np.round(a))
Output:
[-3. -1.  0.  3.]

print(np.clip(a, -2, 2))
Output:
[-2.  -1.2  0.3  2. ]

print(np.floor(a))
Output:
[-3. -2.  0.  2.]

print(np.ceil(a))
Output:
[-2. -1.  1.  3.]

print(np.abs(a))
Output:
[2.7 1.2 0.3 2.6]

print(np.sign(a))
Output:
[-1. -1.  1.  1.]

b = np.array([10, 15, 20])
print(np.mod(b, 3))
Output:
[1 0 2]

print(np.remainder(b, 3))
Output:
[1 0 2]

print(np.logspace(0, 2, 5))
Output:
[  1.           3.16227766  10.          31.6227766  100.        ]

print(np.linspace(0, 1, 5))
Output:
[0.   0.25 0.5  0.75 1.  ]"""


#-----------------------------Interpolation--------------------
"""x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 4, 9])
x_new = np.array([0.5, 1.5, 2.5])
print(np.interp(x_new, x, y))"""






