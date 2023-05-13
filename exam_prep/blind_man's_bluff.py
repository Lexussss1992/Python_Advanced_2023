rows, cols = [int(x) for x in input().split()]
matrix = []
dimensions_row_col = []

for x in range(rows):
    matrix.append([])
    for index, item in enumerate(input().split()):
        matrix[x].append(item)
        if item =='B':
            dimensions_row_col.append(x)
            dimensions_row_col.append(index)

command = input()

while command != 'Finish':
    if command == 'up':
        pass
    elif command == 'down':
        pass
    elif command == 'right':
        pass
    elif command == 'left':
        pass
# 5 8
# - - - O - P - O
# - P - O O - - -
# - - - - - - O -
# - P B - O - - O
# - - - O - - - -
