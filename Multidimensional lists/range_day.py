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

    if data == 2:
        direction = data[0]
        steps = int(data[1])
    else:
        direction = data[0]

    if direction == 'move':
        pass
    elif direction == 'shoot':
        pass

print(coordinates)
print(matrix)