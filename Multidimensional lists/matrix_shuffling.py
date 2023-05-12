from collections import deque

rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for u in range(rows)]
user_input = deque([x for x in input().split()])
command, coordinates = user_input.popleft(), [int(x) for x in user_input]

while command != 'END':
    if command == 'swap' and len(coordinates) == 4:
        if coordinates[0] <= cols and coordinates[1] <= rows and coordinates[2] <= cols and coordinates[3] <= rows:
            el1 = matrix[coordinates[0]][coordinates[1]]
            el2 = matrix[coordinates[2]][coordinates[3]]
            matrix[coordinates[2]][coordinates[3]] = el1
            matrix[coordinates[0]][coordinates[1]] = el2
            for item in matrix:
                print(*item, end='\n')
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    user_input = deque([x for x in input().split()])
    command, coordinates = user_input.popleft(), [int(x) for x in user_input]