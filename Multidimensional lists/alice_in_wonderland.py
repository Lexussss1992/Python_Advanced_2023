n = int(input())
matrix = [input().split() for i in range(n)]
coordinates = []

for i in range(len(matrix)):
    for x in range(len(matrix[i])):
        if matrix[i][x] == 'A':
            coordinates.append(i)
            coordinates.append(x)

print(matrix)
print(coordinates)