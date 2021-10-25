import numpy as np


a = np.array(np.arange(24)).reshape(2,3,4)
print(a)

b=np.append(a, [5,6,7,8])
print(b)
print(b.shape)
b.reshape((7,4))
print(a)

c = np.array(np.arange(24)).reshape(2,3,4) * 10 + 3
print(c)

np.append(a,c, axis=0)
np.append(a,c, axis=0).shape
np.append(a,c, axis=1)
np.append(a,c, axis=1).shape
np.append(a,c, axis=2)
np.append(a,c, axis=2).shape

my_hay_stack = np.hstack((a,c))
print(my_hay_stack)

print(a)
print(c)

after_insert_array = np.insert (c, 1, 444, axis=0)
print(after_insert_array)

np.insert (c, 1, 444, axis=1)
np.insert (c, 1, 444, axis=2)

d = np.empty(c.shape)
np.copyto(d, c)
print(d)

np.delete(d, 1, axis=0)
np.delete(d, 1, axis=1)
np.delete(d, 1, axis=2)
