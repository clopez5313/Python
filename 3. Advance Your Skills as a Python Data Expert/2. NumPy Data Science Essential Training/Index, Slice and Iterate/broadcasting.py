import numpy as np


my_3D_array = np.arange(70)
my_3D_array.shape = (2,7,5)
my_3D_array

# shape
my_3D_array.shape

# number of dimensions
my_3D_array.ndim

# size; number of elements
my_3D_array.size

# data type for each element
my_3D_array.dtype

# Multiply the elements in the 3D array by 5 and then subtract 2.
5 * my_3D_array - 2

# Create two 2D arrays with the specified dimensions and elements.
left_mat = np.arange(6).reshape((2,3))
right_mat = np.arange(15).reshape((3,5))

# Returns an error. The inner function works with 1D arrays.
# np.inner(left_mat, right_mat)

# Returns the product of the two 2D arrays.
np.dot(left_mat, right_mat)

# Returns the sum of all the elements in the 3D array.
my_3D_array.sum()

# Returns the sum of the 2D arrays by rows. Row 0 of array 1 is summed with row 0 of array 2 and so on.
# The result is a 7x5 2D array.
my_3D_array.sum(axis=0)

# Returns the sum of the 2D arrays by columns. All the elements of column 0 of array 1 are summed, then column 1 of array 1
# and so on. The result is a 2x5 2D array.
my_3D_array.sum(axis=1)

# Returns the sum of the 2D arrays by rows. All elements of row 0 of array 1 are summed, then row 1 of array 1 and so on.
# The result is a 2x7 2D array.
my_3D_array.sum(axis=2)

# Creates an array of ones of size 35 that stores integer values, and then converts it into a 7x5 2D array, whose elements
# are all multiplied by 3.
my_2D_array = np.ones(35, dtype='int_').reshape((7,5)) * 3

# Creates a random 7x5 2D array.
my_random_2D_array = np.random.random((7,5))

# NumPy precision is set for 4 decimals, and then the 3D array is multiplied with the random 2D array.
np.set_printoptions(precision=4)
my_3D_array * my_random_2D_array

# Create an array between 0 and 4 where each element is multiplied by 7 and then assign arr[0] to be -1.
my_vector = np.arange(5) * 7
my_vector[0] = -1

# Divides the 3D array by the array created above.
my_3D_array / my_vector

# Returns the module of the 3D array and the array created above.
my_3D_array % my_vector
