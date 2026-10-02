import numpy as np

# 1
"""a=np.arange(1,21).reshape(4,5)
print(a)"""

# 2
"""a=np.array([10,15,20,25,30,35,40,45,50])
b=a[a>20]
print(b)"""

# 3
"""a=np.array([1,2,3])
b=np.array([4,5,6])

print("Sum = ",a+b)
print("Sub = ",a-b)
print("Mul = ",a*b)
print("Div = ",a/b)"""

# 4
"""a=np.arange(1,11)
a[a%2!=0]=-1
print(a)"""

# 5
"""a=np.array([1,2,3,4,5])
r=a[::-1]
print(r)"""

# 6
"""a=np.arange(1,17).reshape(4,4)
print(a)
d=np.diagonal(a)
print("\nDiagonal elements: ",d)"""

# 7
"""a=np.array([1,4,5,7,3,7,2,1,9,5,1])
u,c=np.unique(a,return_counts=True)
print("Unique element : ",u)
print("Counts : ",c)"""

# 8
"""a=np.array([35,67,25,89,12,45,78,90])
a[a>50]=0
print(a)"""

# 9
"""a=np.array([45,67,89,12,34,56,78,90])
i=np.argmax(a)                                              
print("Index of Maximum value: ",i)"""

# 10
"""a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print("\nSum along rows: ",np.sum(a,axis=1))
print("Sum along columns: ",np.sum(a,axis=0))"""

# 11
"""a=np.array([1,2,3,4,5,6,7,8,9])
print(a.reshape(3,3))"""

# 12
"""a=np.array([1,2,3,4,5,6,7,8,9])
print("count values divisible by 3: ",np.sum(a%3==0))"""

# 13
"""a=np.array([[3,2,1],[6,5,4],[9,8,7]])
print("\nOriginal array: \n",a)
print("\nSorted array: \n",np.sort(a))"""
 