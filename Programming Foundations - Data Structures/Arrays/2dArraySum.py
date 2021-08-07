# Define a matrix function.
def twoDMatrix(numRows, numColumns):
    result = []
    rowIndex = 0

    for row in range(numRows):
        row = []

        for column in range(numColumns):
            item = int(input(f"Enter the matrix [{rowIndex}][{column}] "))
            row.append(item)
        result.append(row)
        rowIndex += 1
    return result

# Define a function to add matrices.
def sum(A, B):
    output = []
    print("Sum of the matrix is: ")

    for i in range(len(A)):
        row = []

        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output

# Receive rows and columns info. Call matrix function to create each matrix.
rows = int(input("Enter the number of rows: \n"))
columns = int(input("Enter the number of columns: \n"))

print("Enter the first matrix ")
A = twoDMatrix(rows, columns)
print(A)

print("Enter the second matrix ")
B = twoDMatrix(rows, columns)
print(B)

# Sum both matrices
matrixSum = sum(A, B)
print(matrixSum)
