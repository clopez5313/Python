import numpy as np


class AdjacencyMatrix:
    """Given a cell within a magic square, an adjacency matrix calculates the value of an adjacent cell

    an adjacency matrix can also be used to calculate the value of a non-adjacent cell via 'multiplication'
    """

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.matrix = np.ones((dimensions, dimensions), dtype=np.int64)
        self.__prepare_matrix()

    def __prepare_matrix(self):
        for i in range(self.dimensions):
            for j in range(self.dimensions):
                if ((i + j) > (self.dimensions - 2)):
                    self.matrix[i,j] = 1
                else:
                    self.matrix[i,j] = -1

am = AdjacencyMatrix(7).matrix

amm = np.asmatrix(am)
print(amm)

ammt = amm.T
print(ammt)

ammt = amm.I
print(ammt)
