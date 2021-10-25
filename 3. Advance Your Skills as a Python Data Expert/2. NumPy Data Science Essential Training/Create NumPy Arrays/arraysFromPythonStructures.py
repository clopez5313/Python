import numpy as np
import os


# Clear function for the console.
clear = lambda: os.system("cls")

# Verify NumPy version.
print (np.__version__)
clear()

# Create a NumPy array from a Python List and print it. 
my_list = [-17, 0, 4, 5, 9]
my_array_from_list = np.array(my_list)
print(my_array_from_list)
clear()

# Multiply each element in the array by 10.
print(my_array_from_list * 10)
clear()

# Create a NumPy array from a Python Tuple. Here though, the +7j affects the result, and because of that the 14 and the -3.54
# elements both have a +0j in their result.
my_tuple = (14, -3.54, 5+7j)
np.array(my_tuple)

# Multiply the Tuple by 6. The result is that the whole tuple is repeated 6 times.
print(my_tuple * 6)
clear()

# Multiple each element in the array by 6.
print(np.array(my_tuple) * 6)
