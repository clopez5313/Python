import numpy as np


my_start_array = np.array(np.arange(12))
print(my_start_array)

print(np.tile(my_start_array, 3))
print(np.tile(my_start_array, 3).reshape((3,12)))

my_second_array = np.array(np.arange(7))
tile_1 = np.tile(my_second_array, (3, 1))
print(tile_1)

tile_2 = np.tile(tile_1, (2,2))
print(tile_2)

tile_3 = np.tile(tile_2, (3,1))
print(tile_3)

print(my_second_array)

print(np.repeat(my_second_array, 3))

my_repeatable_array = np.array(np.arange(24)).reshape(2,3,4)
print(my_repeatable_array)

print(np.repeat(my_repeatable_array, 2, axis=0))
print(np.repeat(my_repeatable_array, 2, axis=1))
print(np.repeat(my_repeatable_array, 2, axis=2))
