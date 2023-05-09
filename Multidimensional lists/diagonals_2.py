n = int(input())
matrix = []

for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(j + 1)

print(matrix)