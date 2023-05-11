rows, cols = [int(n) for n in input().split()]

matrix = [[x for x in input().split()] for u in range(rows)]

squares = []

for i in range(rows - 1):
    for j in range(cols - 1):
        square = [
            [matrix[i][j]], [matrix[i][j + 1]],
            [matrix[i + 1][j]], [matrix[i + 1][j + 1]],
        ]
        squares.append(square)

overall_count = 0
for item in squares:
    current_list = []
    for char in item:
        current_list.append(char[0])
    if len(set(current_list)) == 1:
        overall_count += 1

print(overall_count)

# 3 4
# A B B D
# E B B B
# I J B B
