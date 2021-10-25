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

class MagicCharacteristics:
    """Characterisitics of a magic hyper square.

        order must be an odd number.
    """

    def __init__(self, dimensions: int, order: int):
        self.dimensions = dimensions
        self.order = order
        self.adjacencyMatrix = AdjacencyMatrix(dimensions)

        modulus = order % 2
        if not 1 == modulus:
            raise Exception("order must be an odd integer")

        self.totalCells = order ** dimensions
        self.maximumValue = self.totalCells - 1

        """ order exponentiated to each integer in rang(dimensions)
            for example [1, 5, 25, 125] for order:5 and dimensions:4
        """
        self.polynomialBase = np.array(order ** np.arange(dimensions), dtype=np.int64)

        __centerCellCoordinate = (order - 1) // 2
        self.centerCellCoordinates = np.ones((dimensions), dtype=np.int64) * __centerCellCoordinate

        # center cell coordinates and values are the same, this is a special case
        self.centerCellValue = np.ones((dimensions), dtype=np.int64) * __centerCellCoordinate

        self.originValue = np.array(self.__prepareOrigin())

    def __prepareOrigin(self) -> list:
        """ The origin is the cell whose coordinates are all equal to zero.
            Every cell has 1 coordinate for each dimension
        """
        offset = ((self.order - 1) // 2) * -1

        tempOriginValue = np.copy(self.centerCellValue)

        for i in range(self.dimensions):
            tempOriginValue += self.adjacencyMatrix.matrix[i] * offset

        tempOriginValue %= self.order

        return tempOriginValue

    def calculate_cell_value(self, cellCoordinates: np.array) -> np.ndarray:
        increment_to_origin = np.sum(self.adjacencyMatrix.matrix * cellCoordinates, axis=1)
        temp = (self.originValue + increment_to_origin) % self.order
        return np.array(temp)

    def calculate_cell_int(self, cellComponents: np.array) -> int:
        tempInt = np.sum(cellComponents * self.polynomialBase)

        return tempInt

print(MagicCharacteristics(3,5))
