import numpy as np


# An array composed by tuples, where the first element represents the description of the attribute, and the second
# element represents the data type.
person_data_def = [('name','S6'),('height','f8'),('weight','f8'), ('age', 'i8')]

# Creates an array of zeros where each element in the array will be a tuple that will contain each of the data types
# defined in the previous step. Each element will be initialized to the default value of its data type.
people_array = np.zeros((4,), dtype=person_data_def)

# Elements in the array are replaced with a tuple that contains a sample of each of the data types required.
people_array[3] = ('Delta', 73, 205, 34)
people_array[0] = ('Alpha', 65, 112, 23)

# Returns all the elements between the start and the end of the array.
people_array[0:]

# Returns all the elements related to "Age" in the array.
ages = people_array['age']

# Divides all the elements in the array above by 2. It does not affect the original People array, nor the Ages array.
make_youthful = ages / 2
make_youthful

# Creates a 3D array of zeros where each element in the array will be a tuple that will contain each of the data types
# defined in the previous step. Each element will be initialized to the default value of its data type.
people_big_array = np.zeros((4,3,2), dtype=person_data_def)

# Replaces the element in the fourth matrix (index 3), row 2 and column 1 with the data being passed.
people_big_array[3,2,1] = ('Echo', 68, 155, 46)

# Returns all the elements related to "Height" in the array.
people_big_array['height']

# Returns all the elements related to "Height" and "Weight" in the array.
people_big_array[['height', 'weight']]

# Creating a record array.
person_record_array = np.rec.array([('Delta', 73, 205, 34),('Alpha', 65, 112, 23)],dtype=person_data_def)

# Return the "Age" of the first element in the record array.
person_record_array[0].age
