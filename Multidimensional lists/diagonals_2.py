n = int(input())
matrix = []

for i in range(n):
    matrix.append([])
    for j in range(1, n + 1):
        matrix[i].append(j + (i * 3))

print(matrix)