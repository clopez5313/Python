import numpy as np


# truncated binomial: returns (x+1)**3 - (x)**3
def truncated_binomial(x):
    return (x+1)**3 - (x)**3

print(np.testing.assert_equal (truncated_binomial(4), 61))
#print(np.testing.assert_equal (truncated_binomial(4), 65))

my_numpy_function = np.frompyfunc(truncated_binomial, 1, 1)
print(my_numpy_function)

test_array = np.arange(10)
print(test_array)
print(my_numpy_function(test_array))

big_test_array = np.outer(test_array, test_array)
print(big_test_array)
print(my_numpy_function(big_test_array))
