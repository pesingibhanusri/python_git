
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


primary_sum = 0
secondary_sum = 0


for i in range(len(matrix)):
    primary_sum += matrix[i][i]  
    secondary_sum += matrix[i][len(matrix) - 1 - i]  # Secondary diagonal

print("Primary Diagonal Sum:", primary_sum)
print("Secondary Diagonal Sum:", secondary_sum)






matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8, 9],
    [10, 11, 12]
]


result = []


for i in range(len(matrix1)):
    row = []  
    for j in range(len(matrix1[0])):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

for row in result:
    print(row)
