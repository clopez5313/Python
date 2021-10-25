import numpy as np


my_start_array = np.array(np.arange(24))
my_3_8_array = my_start_array.reshape((3,8))
my_2_3_4_array = my_3_8_array.reshape((2,3,4))

print(my_start_array)
print(np.transpose(my_start_array))

print(my_3_8_array)
print(np.transpose(my_3_8_array))

print(my_2_3_4_array)
print(np.transpose(my_2_3_4_array, axes=(0,2,1)))
print(np.transpose(my_2_3_4_array, axes=(2,1,0)))

print(np.swapaxes(my_2_3_4_array, 1, 0))
print(my_2_3_4_array)
print(np.swapaxes(my_2_3_4_array, 1, 0).shape)

print(np.swapaxes(my_2_3_4_array, 2, 1))
print(np.swapaxes(my_2_3_4_array, 2, 0))

print(my_2_3_4_array)
print(np.rollaxis(my_2_3_4_array, 0, 2))
print(np.rollaxis(my_2_3_4_array, 0, 2).shape)
