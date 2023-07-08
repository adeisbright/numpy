import numpy as np

"""
Numpy short for Numerical Python provides a powerful 
data structure known as the array , similar to python 
list. 
Python's list is powerful but it has drawbacks when intended 
to be used for list computations such as adding matrices 
together. 
In Python's list, adding two list together extends the list 
whereas in Numpy, a scalar addition of the array takes place.
You can also subset a Numpy array. 
"""

height = [1, 4, 3]
second_height = [3, 1, 2]
add_heights = np.array(height) + np.array(second_height)
np_height = np.array(height)
print(np_height)
print(add_heights)
even_height = np_height[np_height % 2 == 0]
print(even_height)
double_height = np_height*2
print(double_height)
np_weight = np.array([1, 10, 5])
print(np_weight)
bmi = np_weight/np_height**2
print(bmi)

# A Numpy array must contain elements of same type
# else a type coercion will be performed where
# all elements will be converted to same type
# The arithmetic operations have different function from a
# normal python list
# They do scalar operations on each of the array
# type(nparray) will return numpy.ndarray
# We can create an ndimensional array using Numpy

np_2d_array = np.array([
    [1, 2, 3, 5, 9],
    [2, 4, 6, 8, 7]
])

print(np_2d_array.shape)
# Subsetting an Nd Array
# You can subset using regular python subsetting trick or
# use [row column ] trick
print(np_2d_array[0][1], np_2d_array[0, 1])
print(np_2d_array[:, 1:3])
print(np_2d_array[1:])

"""
# Print out the 50th row of np_baseball
print(np_baseball[:50])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[124][0])
"""

# You can also use numpy to run statistics
# mead, median, std , corrcoef , median , etc
col_one = np_2d_array[:, 0]
print(np.mean(col_one))
print(np.median(col_one))
