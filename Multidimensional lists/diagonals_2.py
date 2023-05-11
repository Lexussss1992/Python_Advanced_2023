n = int(input())
matrix = []

# for i in range(n):
#     matrix.append([])
#     for j in range(1, n + 1):
#         matrix[i].append(j + (i * 3))

for row in range(n):
    lines = [int(x) for x in input().split(', ')]
    matrix.append(lines)

primary_diagonal = 0
secondary_diagonal = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        primary_diagonal += matrix[i] +