rows, cols = [int(x) for x in input().split()]
matrix = []
dimensions_row_col = []
players_touched = 0
moves_count = 0
total_players = 3

for x in range(rows):
    matrix.append([])
    for index, item in enumerate(input().split()):
        matrix[x].append(item)
        if item == 'B':
            dimensions_row_col.append(x)
            dimensions_row_col.append(index)

command = input()

while command != 'Finish':
    if command == 'up':
        if dimensions_row_col[0] - 1 < 0 or matrix[dimensions_row_col[0] - 1][dimensions_row_col[1]] == 'O':
            command = input()
            continue
        else:
            if matrix[dimensions_row_col[0] - 1][dimensions_row_col[1]] == 'P':
                matrix[dimensions_row_col[0]][dimensions_row_col[1]] = '-'
                matrix[dimensions_row_col[0] - 1][dimensions_row_col[1]] = 'B'
                players_touched += 1
                moves_count += 1
                dimensions_row_col[0] -= 1
            elif matrix[dimensions_row_col[0] - 1][dimensions_row_col[1]] == '-':
                matrix[dimensions_row_col[0]][dimensions_row_col[1]] = '-'
                matrix[dimensions_row_col[0] - 1][dimensions_row_col[1]] = 'B'
                moves_count += 1
                dimensions_row_col[0] -= 1
    elif command == 'down':
        if dimensions_row_col[0] + 1 > rows or matrix[dimensions_row_col[0] + 1][dimensions_row_col[1]] == 'O':
            command = input()
            continue
        else:
            if matrix[dimensions_row_col[0] + 1][dimensions_row_col[1]] == 'P':
                matrix[dimensions_row_col[0]][dimensions_row_col[1]] = '-'
                matrix[dimensions_row_col[0] + 1][dimensions_row_col[1]] = 'B'
                players_touched += 1
                moves_count += 1
                dimensions_row_col[0] += 1
            elif matrix[dimensions_row_col[0] + 1][dimensions_row_col[1]] == '-':
                matrix[dimensions_row_col[0]][dimensions_row_col[1]] = '-'
                matrix[dimensions_row_col[0] + 1][dimensions_row_col[1]] = 'B'
                moves_count += 1
                dimensions_row_col[0] += 1
    elif command == 'right':
        if dimensions_row_col[1] + 1 > cols or matrix[dimensions_row_col[0]][dimensions_row_col[1] + 1] == 'O':
            command = input()
            continue
        else:
            if matrix[dimensions_row_col[0]][dimensions_row_col[1] + 1] == 'P':
                matrix[dimensions_row_col[0]][dimensions_row_col[1]] = '-'
                matrix[dimensions_row_col[0]][dimensions_row_col[1] + 1] = 'B'
                players_touched += 1
                moves_count += 1
                dimensions_row_col[1] += 1
            elif matrix[dimensions_row_col[0]][dimensions_row_col[1] + 1] == '-':
                matrix[dimensions_row_col[0]][dimensions_row_col[1]] = '-'
                matrix[dimensions_row_col[0]][dimensions_row_col[1] + 1] = 'B'
                moves_count += 1
                dimensions_row_col[1] += 1
    elif command == 'left':
        if dimensions_row_col[1] - 1 < 0 or matrix[dimensions_row_col[0]][dimensions_row_col[1] - 1] == 'O':
            command = input()
            continue
        else:
            if matrix[dimensions_row_col[0]][dimensions_row_col[1] - 1] == 'P':
                matrix[dimensions_row_col[0]][dimensions_row_col[1]] = '-'
                matrix[dimensions_row_col[0]][dimensions_row_col[1] - 1] = 'B'
                players_touched += 1
                moves_count += 1
                dimensions_row_col[1] -= 1
            elif matrix[dimensions_row_col[0]][dimensions_row_col[1] - 1] == '-':
                matrix[dimensions_row_col[0]][dimensions_row_col[1]] = '-'
                matrix[dimensions_row_col[0]][dimensions_row_col[1] - 1] = 'B'
                moves_count += 1
                dimensions_row_col[0] += 1
    if players_touched == total_players:
        break
    command = input()

print('Game over!')
print(f'Touched opponents: {players_touched} Moves made: {moves_count}')

# 5 8
# - - - O - P - O
# - P - O O - - -
# - - - - - - O -
# - P B - O - - O
# - - - O - - - -
# up
# up
# left
# Finish
#
# 4 4
# O B O -
# - P O P
# - - P -
# - - - -
# left
# right
# down
# right
# down
# right
# up
# right
# up
# down
# Finish
