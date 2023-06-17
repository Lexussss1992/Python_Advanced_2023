N, M = map(int, input().split(','))

matrix = []
coordinates = []
num_cheese = 0
curr_num_cheese = 0
for _ in range(N):
    row = list(input())
    matrix.append(row)

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'M':
            coordinates.append(i)
            coordinates.append(j)
        elif matrix[i][j] == 'C':
            num_cheese += 1

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input()
flag = True

while flag:

    if command == 'danger':
        flag = False
        print('Mouse will come back later!')
        continue

    row = coordinates[0] + directions[command][0]
    col = coordinates[1] + directions[command][1]
    matrix[coordinates[0]][coordinates[1]] = '*'

    if not (0 <= row < N and 0 <= col < M):  # проверяваме дали позицията, на която искаме да стъпим е валидна
        print('No more cheese for tonight!')
        break

    position = matrix[row][col]

    if position == '@':
        command = input()
        continue
    else:
        coordinates = [row, col]
        matrix[coordinates[0]][coordinates[1]] = '*'

    if position == 'C':
        curr_num_cheese += 1
        position = '*'
        if curr_num_cheese == num_cheese:
            print('Happy mouse! All the cheese is eaten, good night!')
            flag = False
            break
    elif position == 'T':
        print('Mouse is trapped!')
        flag = False
        matrix[coordinates[0]][coordinates[1]] = 'M'
        break

    command = input()

matrix[coordinates[0]][coordinates[1]] = 'M'

for i in matrix:
    print(*i, sep='')

# 5,5
# **M**
# T@@**
# CC@**
# **@@*
# **CC*
# left
# down
# left
# down
# down
# down
# right
# danger

# 4,8
# CC@**C*M
# T*@**CT*
# **@@@@**
# T***C***
# down
# right
# left
# down
# left
# danger

# 6,3
# @CC
# @TC
# @C*
# @M*
# @**
# @**
# left
# up
# left
# right
# up
# up
# left
# left
# danger