import numpy as np
from sympy import init_session


## Given this array, find the next number in the sequence
my_teaser_array = np.array([1, 7, 19, 37, 61, 91, 127, 169, 217, 271, 331])
print(my_teaser_array)

print(np.diff(my_teaser_array))
print(np.diff(my_teaser_array, n=2))
print(np.diff(my_teaser_array, n=3))

print(init_session())

diff(x**3)
diff(x**3, x, 2)
diff(x**3, x, 3)
diff(x**3, x, 4)

def my_guess(n):
    return (n+1)**3 - n**3

my_guess(np.arange(20))

my_teaser_array = np.array([1, 7, 19, 37, 61, 91, 127, 169, 217, 271, 331])
my_teaser_array
