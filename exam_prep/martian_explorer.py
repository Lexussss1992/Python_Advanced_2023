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

    if not(0 <= row < SIZE and 0 <= col < SIZE):
        break

    coordinates = [row, col]
    position = matrix[row][col]
    matrix[row][col] = '-'

    check_deposits(position, coordinates)

print(deposits)