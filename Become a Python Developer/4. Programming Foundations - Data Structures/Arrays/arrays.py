# Declaring and importing the module.
# from array import *
import array as arr

# Initializing and accessing array elements.
newArray = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 10])
size = len(newArray)
print("First Element: ", newArray[0])
print("Second Element: ", newArray[1])
print("Second Last Element: ", newArray[size-2])

# Change first element.
newArray[0] = 0
print(newArray)

# Change from third to fifth element.
newArray[2:5] = arr.array('i', [4, 6, 8])
print(newArray)

# Remove the third element.
del newArray[2]
print(newArray)

# Concatenate two arrays.
otherArray = arr.array('i', [9, 11, 12, 14, 15, 16])
finalArray = arr.array('i')
finalArray = newArray + otherArray
print("The concatenated array is: ", finalArray)
