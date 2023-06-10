from collections import deque


def check_deposits(position, coordinates):
    if position == 'R':
        print(f'"Rover got broken at ({coordinates})"')
        return False

    if position == 'W':
        print(f'"Water deposit found at ({coordinates})"')
        deposits['W'] += 1

    if position == 'M':
        print(f'"Metal deposit found at ({coordinates})"')
        deposits['M'] += 1

    if position == 'C':
        print(f'"Concrete deposit found at ({coordinates})"')
        deposits['C'] += 1


def check_coordinates(SIZE, row, col):
    if row > SIZE - 1:
        pos = [0, col]
    elif row < 0:
        pos = [5, col]
    elif col > SIZE - 1:
        pos = [row, 0]
    elif col < 0:
        pos = [row, 5]
    else:
        pos = [row, col]

    return pos


SIZE = 6

matrix = [input().split() for i in range(SIZE)]
coordinates = []

for i in range(len(matrix)):
    for j in range(i):
        if matrix[i][j] == 'E':
            coordinates.append(i)
            coordinates.append(j)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

deposits = {
    'W': 0,
    'M': 0,
    'C': 0
}

commands = deque(input().split(', '))

while commands:
    command = commands.popleft()

    row = coordinates[0] + directions[command][0]
    col = coordinates[1] + directions[command][1]

    coordinates = check_coordinates(SIZE, row, col)
    position = matrix[row][col]
    matrix[row][col] = '-'

    check_deposits(position, coordinates)

print(deposits)