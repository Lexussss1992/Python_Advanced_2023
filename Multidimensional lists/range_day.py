matrix = [input().split() for i in range(5)]
number_of_commands = int(input())
coordinates = []

for i in range(len(matrix)):
    for j in range(i):
        if matrix[i][j] == 'A':
            coordinates.append(i)
            coordinates.append(j)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for i in range(number_of_commands):
    first_command, *data = [i for i in input().split()]
    direction = data[0]
    steps = data[1] if len(data) == 2 else []

    print(first_command)
    print(direction)
    print(steps)

print(coordinates)
print(matrix)