rows, cols = [int(x) for x in input().split()]
matrix = []

for i in range(rows):
    matrix.append([])
    for j in input().split():
        matrix[i].append(int(j))

matrices = []

for i in range(rows - 2):
    for j in range(cols - 2):
        three_by_three_matrix = [
            matrix[i][j], matrix[i][j + 1], matrix[i][j + 2],
            matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2],
            matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]
        ]
        matrices.append(three_by_three_matrix)

sum = 0
biggets_matrix = []

for i in range(len(matrices)):
    sum_matrix = 0
    for j in matrices[i]:
        sum_matrix += j
    if sum_matrix >= sum:
        sum = sum_matrix
        biggets_matrix = matrices[i]

print(f'Sum = {sum}')

for index, item in enumerate(biggets_matrix, start=1):
    print(item, end=' ' if index % 3 else '\n')

# 5 6
# 1 0 4 3 1 1
# 1 3 1 3 0 4
# 6 4 1 2 5 6
# 2 2 1 5 4 1
# 3 3 3 6 0 5