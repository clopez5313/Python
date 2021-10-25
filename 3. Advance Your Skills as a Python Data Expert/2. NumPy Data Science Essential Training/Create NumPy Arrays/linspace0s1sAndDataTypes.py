import numpy as np
import os


# Clear function for the console.
clear = lambda: os.system("cls")

# Creates an array between 5 and 15 evenly divided by 9 elements.
np.linspace(5, 15, 9)

# Returns a NumPy array with the array created by linspace on the position 0, and the size of repstep in position 1.
my_linspace = np.linspace(5, 15, 9, retstep=True)
my_linspace[1]

# Same operation as above, but shorter.
np.linspace(5, 15, 9, retstep=True)[1]

# Creates an array of size 5 with all elements set to 0. Elements are float though.
np.zeros(5)

# Creates an array of size 7 with all elements set to 1. Elements are float though.
np.ones(7)

# Create a 2D array of zeros with 5 rows and 4 columns.
np.zeros((5,4))

# Create a 3D array of zeros. 5 matrices with 4 rows and 3 columns.
np.zeros((5,4,3))

# Creates an array of zeros that will use integers instead of float.
np.zeros(11, dtype='int64')
