import numpy as np


mi_casa = np.array([-45, -31, -12, 0, 2, 25, 51, 99])
su_casa = mi_casa

#reference equality
print(mi_casa is su_casa)

print(id(mi_casa))
print(id(su_casa))

#value inequality
print(mi_casa == su_casa)

su_casa[4] = 1010
print(su_casa)
print(mi_casa)

tree_house = np.array([-45, -31, -12, 0, 2, 25, 51, 99])

print(tree_house == mi_casa)

print(id(tree_house))
print(id(mi_casa))

tree_house[0] = 214
print(tree_house)
print(mi_casa)
print(tree_house == mi_casa)
print(tree_house is mi_casa)

# Shallow Copy

farm_house = tree_house.view()
farm_house.shape = (2,4)
print(tree_house)
print(farm_house)
tree_house [3] = -111
print(farm_house)

# Deep Copy

dog_house = np.copy(tree_house)
dog_house[0] = -121
print(dog_house)

print(tree_house)
