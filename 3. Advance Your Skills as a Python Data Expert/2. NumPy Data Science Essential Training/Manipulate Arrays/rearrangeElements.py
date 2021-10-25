import numpy as np


my_start_array = np.array(np.arange(24))
my_3_8_array = my_start_array.reshape((3,8))
my_2_3_4_array = my_3_8_array.reshape((2,3,4))

print(my_3_8_array)
np.fliplr(my_3_8_array)

print(my_2_3_4_array)

np.fliplr(my_2_3_4_array)
np.flipud(my_3_8_array)
np.flipud(my_2_3_4_array)

print(my_start_array)

np.roll(my_start_array, 5)
np.roll(my_start_array, -5)
np.roll(my_2_3_4_array, 2)
np.roll(my_2_3_4_array, -2)
print(my_3_8_array)

np.rot90(my_3_8_array)
np.rot90(my_3_8_array, k=-1)
