import numpy as np


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(a)

together = np.concatenate((a, b), axis=0)
print(together)

print(together.shape)

together[1,1] = 555
print(together)
print(a)

c = np.array([[1, 2], [3, 4]]) *3 + 5
print(c)

np.concatenate((a, c), axis=1)

arrays = np.zeros((5,3,4))
for n in range(5):
    arrays[n] = np.random.randn(3, 4)

print(arrays)

stack0 = np.stack(arrays, axis=0)
stack1 = np.stack(arrays, axis=1)
stack2 = np.stack(arrays, axis=2)

my_stacks = np.array([stack0.shape, stack1.shape, stack2.shape])
print(my_stacks)

print(stack0)
print(stack1)
print(stack2)

temp = np.arange(5)
np.split(temp,1)

before_split = stack0
print(before_split.shape)

s0=np.split (before_split, 5, axis=0)
print(s0)

print(type(s0))

print(s0[1])

print(s0[1].shape)

s1=np.split (before_split, 3, axis=1)
print(s1)

s2=np.split (before_split, 4, axis=2)
print(s2)
