import numpy as np


np.set_printoptions(precision=2)

# note double underscrore
print(np.__version__)

my_array = np.array(np.arange(10))
print(my_array)
print(my_array[::-1])
print(my_array * 3)

### Create array with 20 zeros; every fifth element equals four
my_array = np.zeros(20)
my_array[0::5] = 4
print(my_array)

### Create a 3x3 matrix whose elements equal 0 through 8
my_matrix = np.asmatrix(np.array(np.arange(9)).reshape((3,3)))
print(my_matrix)

### Transpose the rows and columns
print(my_matrix.T)

### Create a 5x5 identity matrix with integer components
my_matrix = np.asmatrix(np.eye(5, dtype='int'))
print(my_matrix)

### Find the mean of a vector with 30 random elements.  Can you guess the approximate value for the mean?
my_random_vector = np.random.random(30)
print(my_random_vector.mean())

#### Repeat, and visually estimate the mean for the sum of the two means
my_random_vector = np.random.random(30)
print(my_random_vector.mean())

### Create a 2d array with ones on the border and zeros inside the border
my_bordered_array = np.ones((5,5))
my_bordered_array[1:-1,1:-1] = 0
print(my_bordered_array)

### Create an 8x8 checker board with alternating zeros and ones
my_checker_board = np.zeros((8,8),dtype=int)
my_checker_board[1::2,::2] = 1
my_checker_board[::2,1::2] = 1
print(my_checker_board)

my_alternative_checker_board = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(my_alternative_checker_board)

### Create a sorted vector that contain 'n' random numbers
vector_size = 12
my_random_vector = np.random.random(vector_size)
my_sorted_random_vector = np.sort(my_random_vector)
print (my_sorted_random_vector)

### Without sorting, replace largest element in random array with the value 1234
my_random_vector[my_random_vector.argmax()] = 1234
print(my_random_vector)

### Given the following data type and data set; sort according to 'height'
camelot_dtype = [('name', 'S10'), ('height', float), ('age', int)]
camelot_values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38), ('Galahad', 1.7, 38)]

camelot_structured_array = np.array(camelot_values, dtype=camelot_dtype)
camelot_sorted_array = np.sort(camelot_structured_array, order='height')
for n in np.arange(camelot_sorted_array.size):
    print (camelot_sorted_array[n])

### Make an array read-only (immutable)
my_ordinary_array = np.array(np.arange(12))
#my_ordinary_array.flags.writeable = False
my_ordinary_array[5] = 1234

### Print enumerated values from a 3x3 NumPy array
my_3_3_array = np.arange(9).reshape(3,3)
for index, value in np.ndenumerate(my_3_3_array):
    print(index, value)
