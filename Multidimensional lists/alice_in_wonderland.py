def check_if_valid(matrix, command, coordinates):
    if command == 'right':
        if coordinates[1] > n - 1 or matrix[coordinates[0]][coordinates[1] + 1] == 'R':
            return True
    elif command == 'left':
        if coordinates[1] < 0 or matrix[coordinates[0]][coordinates[1] - 1] == 'R':
            return True
    elif command == 'down':
        if coordinates[0] > n - 1 or matrix[coordinates[0] + 1][coordinates[1]] == 'R':
            return True
    elif command == 'up':
        if coordinates[0] < 0 or matrix[coordinates[0] - 1][coordinates[1]] == 'R':
            return True

n = int(input())
matrix = [input().split() for i in range(n)]
coordinates = []
tea_bags_quantity = 0
tea_bags_number = 0

for i in range(len(matrix)):
    for x in range(len(matrix[i])):
        if matrix[i][x] == 'A':
            coordinates.append(i)
            coordinates.append(x)
            break

while tea_bags_number != 10:
    command = input()
    if check_if_valid(matrix, command, coordinates):
        print("Alice didn't make it to the tea party.")
        break
    if command == 'right':
        if matrix[coordinates[0]][coordinates[1] + 1].isnumeric():
            tea_bags_quantity += int(matrix[coordinates[0]][coordinates[1] + 1])
            tea_bags_number += 1
            matrix[coordinates[0]][coordinates[1] + 1] = 'A'
            matrix[coordinates[0]][coordinates[1]] = '*'
            coordinates[1] += 1
        elif matrix[coordinates[0]][coordinates[1] + 1] == '.':
            matrix[coordinates[0]][coordinates[1] + 1] = 'A'
            matrix[coordinates[0]][coordinates[1]] = '*'
            coordinates[1] += 1
        elif matrix[coordinates[0]][coordinates[1] + 1] == '*':
            matrix[coordinates[0]][coordinates[1] + 1] = 'A'
            matrix[coordinates[0]][coordinates[1]] = '*'
            coordinates[1] += 1
    elif command == 'left':
        if matrix[coordinates[0]][coordinates[1] - 1].isnumeric():
            tea_bags_quantity += int(matrix[coordinates[0]][coordinates[1] - 1])
            tea_bags_number += 1
            matrix[coordinates[0]][coordinates[1] - 1] = 'A'
            matrix[coordinates[0]][coordinates[1]] = '*'
            coordinates[1] -= 1
        elif matrix[coordinates[0]][coordinates[1] - 1] == '.':
            matrix[coordinates[0]][coordinates[1] - 1] = 'A'
            matrix[coordinates[0]][coordinates[1]] = '*'
            coordinates[1] -= 1
        elif matrix[coordinates[0]][coordinates[1] - 1] == '*':
            matrix[coordinates[0]][coordinates[1] - 1] = 'A'
            matrix[coordinates[0]][coordinates[1]] = '*'
            coordinates[1] -= 1
    elif command == 'down':
        if matrix[coordinates[0] + 1][coordinates[1]].isnumeric():
            tea_bags_quantity += int(matrix[coordinates[0] + 1][coordinates[1]])
            tea_bags_number += 1
            matrix[coordinates[0] + 1][coordinates[1]] = 'A'
            matrix[coordinates[0]][coordinates[1]] = '*'
            coordinates[0] += 1
        elif matrix[coordinates[0] + 1][coordinates[1]] == '.':
            matrix[coordinates[0] + 1][coordinates[1]] = 'A'
            matrix[coordinates[0]][coordinates[1]] = '*'
            coordinates[0] += 1
        elif matrix[coordinates[0] + 1][coordinates[1]] == '*':
            matrix[coordinates[0] + 1][coordinates[1]] = 'A'
            matrix[coordinates[0]][coordinates[1]] = '*'
            coordinates[0] += 1
    elif command == 'up':
        if matrix[coordinates[0] - 1][coordinates[1]].isnumeric():
            tea_bags_quantity += int(matrix[coordinates[0] - 1][coordinates[1]])
            tea_bags_number += 1
            matrix[coordinates[0] - 1][coordinates[1]] = 'A'
            matrix[coordinates[0]][coordinates[1]] = '*'
            coordinates[0] -= 1
        elif matrix[coordinates[0] - 1][coordinates[1]] == '.':
            matrix[coordinates[0] - 1][coordinates[1]] = 'A'
            matrix[coordinates[0]][coordinates[1]] = '*'
            coordinates[0] -= 1
        elif matrix[coordinates[0] - 1][coordinates[1]] == '*':
            matrix[coordinates[0] - 1][coordinates[1]] = 'A'
            matrix[coordinates[0]][coordinates[1]] = '*'
            coordinates[0] -= 1

if tea_bags_number == 10:
    print('She did it! She went to the party.')

for i in range(len(matrix)):
    print(*matrix[i])