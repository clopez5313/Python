import numpy as np


my_start_array = np.array(np.arange(24))
print(my_start_array)

print(my_start_array.shape)

my_3_8_array = my_start_array.reshape((3,8))
print(my_3_8_array)

my_3_8_array[0,0] = 1234
print(my_start_array)

my_ravel_array = my_3_8_array.ravel()
print(my_ravel_array)
print(my_ravel_array.shape)

for n in my_3_8_array.flat:
    print(n)
