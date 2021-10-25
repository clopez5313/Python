import numpy as np


my_vector = np.array([-17, -4, 0, 2, 21, 37, 105])

# Checks if the elements in the array are divisible by 7.
zero_mod_7_mask = 0 == (my_vector % 7)

# Returns an array of the elements divisible by 7.
sub_array = my_vector[zero_mod_7_mask]

# Checks the array and returns the elements greater than zero.
sub_array[sub_array>0]

# Check again if the elements in the array are divisible by 7.
mod_test = 0 == (my_vector % 7)

# Check if the elements in the array are greater than zero.
positive_test = my_vector > 0

# Use a Logical AND of the two boolean arrays to retrieve the elements divisible by 7 that are greater than zero.
combined_mask = np.logical_and(mod_test, positive_test)
my_vector[combined_mask]
