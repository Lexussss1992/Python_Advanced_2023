n = int(input())

matrix = []
coordinates = []

for i in range(n):
    matrix.append(input())

for x in range(len(matrix)):
    for j in range(len(matrix[x])):
        if matrix[x][j] == 'K':
            coordinates.append(x)
            coordinates.append(j)

print(matrix)
print(coordinates)