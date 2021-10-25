import numpy as np


def is_integer(x):
    return np.equal(np.mod(x, 1), 0)

numpy_is_integer = np.frompyfunc(is_integer, 1, 1)

number_of_triangles = 9

base = np.arange(number_of_triangles) + 1
height = np.arange(number_of_triangles) + 1

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.ufunc.outer.html
hypotenuse_squared = np.add.outer(base ** 2, height ** 2)
hypotenuse = np.sqrt(hypotenuse_squared)

print(numpy_is_integer(hypotenuse))
