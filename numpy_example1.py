import numpy as np 

list1 = [1 , 2 , 3 , 4 , 5 , 6]  

numpy_list = np.array(list1) 
scalar_list = numpy_list*2 
print(numpy_list) 
print(scalar_list)
scalar_list = numpy_list - 2 
print(scalar_list)

# Get the shape of a numpy array 
print(numpy_list.shape) # The result is returend in this tuple form (row,column ) where row tells the number of rows  
print(numpy_list.ndim) # Ge the dimension of a numpy list  

# Slice a numpy array 

subset = numpy_list[1:3] 
print(subset)

two_dimension = np.array([
    [1 , 2 , 3 , 4 , 5 , 6 ,7] , 
    [8,9,10,11,12,13,14]
])

shape2 = two_dimension.shape
datatype = two_dimension.dtype
element_count = two_dimension.size 
print("The shape of the above ndarray is {} while the types are {}  and size is {}".format(shape2 , datatype , element_count)) 

slicer = two_dimension[0][1] # Same as two_dimension[0,1]

print(slicer)

# Slicing a multi array 
slicer = two_dimension[ : , 1] # Returns items at index 1 for both arrays 
print(slicer)
slicer = two_dimension[  0  , 1  : 5] 
print(slicer)

# Examining Dot Product 
ll1 = [1 , 2 , 3 ] 
ll2 = [4 , 5 , 6]

a = np.array(ll1) 
b = np.array(ll2)

dot = 0 

for i in range(len(ll1)):
    dot += ll1[i] * ll2[i] 

print(dot) 
dot = np.dot(a , b)
print(dot)

aa = np.array([10 , 20  ,19 , 30]) 

even = np.argwhere(a%2 == 0).flatten() 

bb =  aa[even] 

print(bb)

# Reshaping a numpy arran 
a3 = np.arange(1 , 7)

print(a3)

b3 = a3.reshape(2 ,3) 

# print(b3)
b3 = a[: , np.newaxis]

print(b3)

# Concatenating arrays 

a4 =  np.array([[1, 2], [3, 4]])
a41 = np.array([[5, 6]])

a42 = np.concatenate((a4 , a41))
print(a42)

# Working with some statistics 
a5 = np.array([[7,8,9,10,11,12,13] , [17,18,19,20,21,22,23]]) 

print(a5.sum())
print(a5.sum(axis=1)) # Sums each array, and returns the result . Since we have two arrays, it returns two summation. one for each 

print(a5.min()) 
print(a5.mean())

zeros = np.zeros((3 , 2)) 
print(zeros) 

ones = np.ones((4 , 3)) 
print(ones)
full = np.full(6 , 4)
print(full)

randomer = np.random.random((3,2) ) 
print(randomer) 

rand = np.random.random(50) 
print(rand) 

randit = np.random.randint(3 , 10 , size = (3 , 3)) 
print(randit)

a6 = np.array([[3 , 4] , [5 , 6]]) 
eigenvector , eigenvalue = np.linalg.eig(a6)
print(eigenvalue)