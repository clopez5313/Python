import os

# Create elements and read the matrix.
theMatrix = [["Arun", 25, 90, 74],
             ["Sachin", 410, 87.50, 130],
             [56, "Abhinay", 253, 471]]
print("The matrix is: ", theMatrix)

# Read the last element from each row.
matrixLength = len(theMatrix)

for row in range(matrixLength):
    print(theMatrix[row][-1])

os.system("cls")

# Add two matrices.
matrix0 = [[10,13,44],[11,2,3],[5,3,1]]
matrix1 = [[7,16,-6],[9,20,-4],[-1,3,27]]
result = [[0,0,0],[0,0,0],[0,0,0]]
matrixLength = len(matrix0)

for row in range(len(matrix0)):
    for column in range(len(matrix1)):
        result[row][column] = matrix0[row][column] + matrix1[row][column]

print("The sum of matrix 0 and matrix 1 is ", result)

# Multiply two matrices.
for row in range(len(matrix0)):
    for column in range(len(matrix1)):
        result[row][column] = matrix0[row][column] * matrix1[row][column]

print("The multiplication of matrix 0 and matrix 1 is ", result)
os.system("cls")

# Transpose of a matrix.
matrix2 = [[12, 7], [4, 5], [3, 8]]
result = [[0,0,0], [0,0,0]]

for row in range(len(matrix2)):
    for column in range(len(matrix2[0])):
        result[column][row] = matrix2[row][column]

for r in result:
    print(r)

# Transpose using list comprehension.
os.system("cls")
result = [[matrix2[column][row] for column in range(len(matrix2))] for row in range(len(matrix2[0]))]

for r in result:
    print(r)
