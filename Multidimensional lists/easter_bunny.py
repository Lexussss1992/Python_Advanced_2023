n = int(input())
matrix = [input().split() for _ in range(n)]
bunny_coordinates = []

for i in range(len(matrix)):
    for x in range(len(matrix[i])):
        if matrix[i][x] == 'B':
            bunny_coordinates.append(i)
            bunny_coordinates.append(x)

dict = {
    'up': [0, []],
    'down': [0, []],
    'left': [0, []],
    'right': [0, []]
}

for x in range(bunny_coordinates[0], -1, -1): #up
    if matrix[x][bunny_coordinates[1]] != 'B':
        if matrix[x][bunny_coordinates[1]] == 'X':
            break
        else:
            for key, value in dict.items():
                if key == 'up':
                    value[1].append([x, bunny_coordinates[1]])
                    value[0] += int(matrix[x][bunny_coordinates[1]])

for i in range(bunny_coordinates[1], len(matrix)): #right
    if matrix[bunny_coordinates[0]][i] != 'B':
        if matrix[bunny_coordinates[0]][i] == 'X':
            break
        else:
            for key, value in dict.items():
                if key == 'right':
                    value[1].append([bunny_coordinates[0], i])
                    value[0] += int(matrix[bunny_coordinates[0]][i])

for i in range(bunny_coordinates[1], 0, -1): #left
    if matrix[bunny_coordinates[0]][i] != 'B':
        if matrix[bunny_coordinates[0]][i] == 'X':
            break
        else:
            for key, value in dict.items():
                if key == 'left':
                    value[1].append([bunny_coordinates[0], i])
                    value[0] += int(matrix[bunny_coordinates[0]][i])

for x in range(bunny_coordinates[0], n): #down
    if matrix[x][bunny_coordinates[1]] != 'B':
        if matrix[x][bunny_coordinates[1]] == 'X':
            break
        else:
            for key, value in dict.items():
                if key == 'down':
                    value[1].append([x, bunny_coordinates[1]])
                    value[0] += int(matrix[x][bunny_coordinates[1]])

max_value = max(dict.values())
max_key = max(dict, key=dict.get)
print(max_key)
for i in max_value[1]:
    print(i)

print(max_value[0])
