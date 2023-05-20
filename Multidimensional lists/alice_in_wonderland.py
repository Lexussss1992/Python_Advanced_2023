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
        if coordinates[0] < 0 or or matrix[coordinates[0] - 1][coordinates[1]] == 'R':
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

while tea_bags_number == 10:
    command = input()
    if check_if_valid(matrix, command, coordinates):
        break
    if command == 'right':
        if matrix[coordinates[0]][coordinates[1] + 1].isnumeric():
            tea_bags_quantity += int(matrix[coordinates[0]][coordinates[1] + 1])
            tea_bags_number += 1
            matrix[coordinates[0]][coordinates[1] + 1] = 'A'
            matrix[coordinates[0]][coordinates[1]] = '*'
            coordinates[1] += 1
        else:
            if matrix[coordinates[0]][coordinates[1] + 1] == 'R':
                break
            elif matrix[coordinates[0]][coordinates[1] + 1] == '-':
                pass
    elif command == 'left':
        pass
    elif command == 'down':
        pass
    elif command == 'up':
        pass