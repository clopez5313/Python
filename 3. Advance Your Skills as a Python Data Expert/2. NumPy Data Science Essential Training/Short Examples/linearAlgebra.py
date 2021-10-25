import numpy as np
from numpy.linalg import solve
from numpy.linalg import eig


my_first_matrix = np.matrix([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
print(my_first_matrix)

# transpose
print(my_first_matrix.T)

# matrix inverse
my_first_inverse = my_first_matrix.I
print(my_first_inverse)

#should return inverse; floating point values "almost" equal zero
print(my_first_matrix * my_first_inverse)

# create an identity matrix
np.eye(5)

# Solve simultaneous linear equations
right_hand_side = np.matrix([[11],
                             [22],
                             [33]])

# not efficient; use only for small matrices
solution = my_first_inverse * right_hand_side
print(solution)

# confirm that solution is correct
print(my_first_matrix * solution - right_hand_side)

# more efficient for large matrices
print(solve(my_first_matrix, right_hand_side))

# Compute the eigenvalues and right eigenvectors
print(eig(my_first_matrix))
