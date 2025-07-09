# Basic 2D matrix operations
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print("Matrix:")
for row in matrix:
    print(row)

# Transpose
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transpose:")
for row in transpose:
    print(row)