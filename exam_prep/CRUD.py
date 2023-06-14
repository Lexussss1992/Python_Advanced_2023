SIZE = 6

matrix = [input().split() for x in range(SIZE)]
coordinates = input()
position = [int(i) for i in coordinates if i.isnumeric()]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input().split(', ')

while command[0] != 'Stop':
    first_command, *data = command
    direction = data[0]
    letter = data[1] if len(data) == 2 else 0

    row = position[0] + directions[direction][0]
    col = position[1] + directions[direction][1]
    position = [row, col]

    if first_command == 'Create':
        if matrix[row][col] == '.':
            matrix[row][col] = letter
    elif first_command == 'Update':
        if matrix[row][col] != '.':
            matrix[row][col] = letter
    elif first_command == 'Read':
        if matrix[row][col] != '.':
            print(matrix[row][col])
    elif first_command == 'Delete':
        if matrix[row][col] != '.':
            matrix[row][col] = '.'

    command = input().split(', ')

for i in matrix:
    print(*i)

# . . . . . .
# . 6 . . . .
# G . S . t S
# . . 10 . . .
# . 95 . . 8 .
# . . P . . .
# (1, 1)
# Create, down, r
# Update, right, e
# Create, right, a
# Read, right
# Delete, right
# Stop

# H 8 . . . .
# 70 i . . . .
# t . . . B .
# 50 . 16 . C .
# . . . t . .
# . 25 . . . .
# (0, 0)
# Read, right
# Read, down
# Read, left
# Delete, down
# Create, right, 10
# Read, left
# Stop