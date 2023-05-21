matrix = [input().split() for i in range(5)]
number_of_commands = int(input())
coordinates = []

for i in range(len(matrix)):
    for j in range(i):
        if matrix[i][j] == 'A':
            coordinates.append(i)
            coordinates.append(j)

directions = {
    'up': [0, -1],
    'down': [0, 1],
    'left': [0, -1],
    'right': [0, 1]
}

for i in range(number_of_commands):
    first_command, *data = [i for i in input().split()]
    direction = data[0]
    steps = int(data[1]) if len(data) == 2 else 0
    directions[direction][0] = steps

    row = coordinates[0] + (directions[direction][0] * directions[direction][1])
    col = coordinates[1] + (directions[direction][0] * directions[direction][1])

    print(row)
    print(col)


print(coordinates)
print(matrix)
print(directions)