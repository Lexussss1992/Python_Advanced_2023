n = int(input())
matrix = [input().split() for i in range(n)]
coordinates = []
tea_bags_quantity = 0

for i in range(len(matrix)):
    for x in range(len(matrix[i])):
        if matrix[i][x] == 'A':
            coordinates.append(i)
            coordinates.append(x)
            matrix[i][x] = '*'
            break

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while tea_bags_quantity < 10:
    command = input()

    row = coordinates[0] + directions[command][0]
    col = coordinates[1] + directions[command][1]

    if not(0 <= row < n and 0 <= col < n):
        break

    coordinates = [row, col]
    position = matrix[row][col]
    matrix[row][col] = '*'

    if position == 'R':
        break

    if position.isnumeric():
        tea_bags_quantity += int(position)

if tea_bags_quantity < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

print(*[' '.join(row) for row in matrix], sep='\n')

