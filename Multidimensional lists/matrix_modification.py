def check_coordinates(coordinates):
    coordinates = [int(x) for x in coordinates]
    if 0 <= coordinates[0] <= len(matrix) - 1 and 0 <= coordinates[1] <= len(matrix) - 1:
        return True


def modify_matrix(matrix, command, coordinates):
    if command == 'Add':
        matrix[coordinates[0]][coordinates[1]] += coordinates[2]
    elif command == 'Subtract':
        matrix[coordinates[0]][coordinates[1]] -= coordinates[2]
    return matrix

n = int(input())
matrix = []

for i in range(n):
    matrix.append([int(x) for x in input().split()])

command, *coordinates = [x for x in input().split()]
coordinates = [int(x) for x in coordinates]

while command != 'END':
    coordinates = [int(x) for x in coordinates]
    if check_coordinates(coordinates):
        modify_matrix(matrix, command, coordinates)
    else:
        print('Invalid coordinates')
    command, *coordinates = [x for x in input().split()]

for el in matrix:
    print(*el, end='\n')