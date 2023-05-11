rows, columns = [int(x) for x in input().split()]
matrix = []
twoBYtwo_matrices = 0
n = 2
for row in range(rows):
    column = [str(x) for x in input().split()]
    matrix.append(column)

for row in range(rows):
    for column in range(columns - 1):
        if matrix[row][column] == matrix[row][column + 1] and matrix[row + 1][column] == matrix[row + 1][column + 1]:
            twoBYtwo_matrices += 1
        else:
            continue

print(twoBYtwo_matrices)

# 3 4
# A B B D
# E B B B
# I J B B
