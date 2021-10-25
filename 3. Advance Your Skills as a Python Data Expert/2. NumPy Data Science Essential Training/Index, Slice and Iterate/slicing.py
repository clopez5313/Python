import numpy as np


# Creates a 2D array from 0 to 34 with 7 rows and 5 columns.
my_array= np.arange(35)
my_array.shape = (7,5)

# Returns all the elements in row 2.
my_array[2]

# Returns element at row 5, column 2.
my_array[5,2]

# Another way of accessing a single element.
row = 5
column = 2
my_array[row, column]

# Another way of accessing a single element.
my_array[5][2]

# Creating a 3D array from 0 to 69, with two matrices of 7 rows and 5 columns.
my_3D_array = np.arange(70)
my_3D_array.shape = (2, 7, 5)

# Returns the second matrix in the 3D array.
my_3D_array[1]

# Returns the elements in the third row of the second matrix.
my_3D_array[1,3]

# Replaces the value of the element at row 3 column 2 of the second matrix, with 1111.
my_3D_array[1,3,2] =1111
