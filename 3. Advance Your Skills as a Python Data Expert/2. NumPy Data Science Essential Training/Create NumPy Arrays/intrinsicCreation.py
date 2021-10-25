import numpy as np
import os


# Clear function for the console.
clear = lambda: os.system("cls")

# Calling arange() by itself will cause a runtime error.
# arange(7)

# An array of integers between 0 and 6.
print(np.arange(7))

# An array of integers between 10 and 22.
np.arange(10, 23)

# Subtract 10 from the range of arange(). The resulting array goes between 0 and 12.
np.arange(10, 23) -10

# Subtract 10 from the range of arange() and add 1. The resulting array goes between 1 and 13.
np.arange(10, 23) -10 +1

# Lenght of the array.
len (np.arange(10, 23))

# Length of the array using the size attribute of NumPy.
my_range_array = np.arange(10, 23)
my_range_array.size

# Calling the size attribute directly.
np.arange(10, 23).size

# Create an array with 5 as the step parameter.
np.arange(10, 23, 5)

# Create an array with 5 as the step parameter.
np.arange(10, 25, 5)

# Create an array with 5 as the step parameter.
np.arange(10, 26, 5)

# Create an array with 5 as the step parameter.
np.arange(26, step=5)

# Create an array with 5 as the step parameter.
np.arange(0, 26, step=5)

# Create an array with 5 as the step parameter.
np.arange(0, 26, 5)
