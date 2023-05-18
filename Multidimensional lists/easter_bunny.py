from collections import defaultdict

n = int(input())
matrix = [input().split() for _ in range(n)]
bunny_coordinates = []

for i in range(len(matrix)):
    for x in range(len(matrix[i])):
        if matrix[i][x] == 'B':
            bunny_coordinates.append(i)
            bunny_coordinates.append(x)

up = 0
up_list = []
right = 0
right_list = []
left = 0
left_list = []
down = 0
down_list = []

dict = {
    'up': [0, []],
    'down': 0,
    'left': 0,
    'right': 0
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
print(dict)
# for i in range(bunny_coordinates[1], len(matrix)): #right
#     if matrix[bunny_coordinates[0]][i] != 'B':
#         if matrix[bunny_coordinates[0]][i] == 'X':
#             break
#         else:
#             right += int(matrix[bunny_coordinates[0]][i])
#             right_list.append([bunny_coordinates[0], i])
#
#
# for i in range(bunny_coordinates[1], 0, -1): #left
#     if matrix[bunny_coordinates[0]][i] != 'B':
#         if matrix[bunny_coordinates[0]][i] == 'X':
#             break
#         else:
#             left += int(matrix[bunny_coordinates[0]][i])
#             left_list.append([bunny_coordinates[0], i])
#
# for x in range(bunny_coordinates[0], n): #down
#     if matrix[x][bunny_coordinates[1]] != 'B':
#         if matrix[x][bunny_coordinates[1]] == 'X':
#             break
#         else:
#             down += int(matrix[x][bunny_coordinates[1]])
#             down_list.append([x, bunny_coordinates[1]])



# 8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22