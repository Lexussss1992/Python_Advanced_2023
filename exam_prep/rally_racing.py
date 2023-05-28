def move(direction):  # създаваме фунцкия move, първи параметър посоката и втори стъпките int
    r = car_poss[0] + (directions[direction][0])  # намираме реда и колоната като умножаваме стойностите от
    c = car_poss[1] + (directions[direction][1])  # посоката по стъпките и събираме с текущите координати

    if not (0 <= r < n and 0 <= c < n):  # проверяваме дали позицията, на която искаме да стъпим е валидна
        return car_poss  # ако не е, връщаме текущата позиция
    if matrix[r][c] == 'T':  # проверяваме дали на позицията, на която искаме да стъпим има мишена
        matrix[r][c] = '.'
        r = tunels_poss[2]
        c = tunels_poss[3]  # ако да, връщаме текущата позиция

    return [r, c]


n = int(input())
racing_number = input()
matrix = [input().split() for i in range(n)]
car_poss = [0, 0]
tunels_poss = []
finish_poss = []
km = 0

for x in range(n):
    for j in range(len(matrix)):
        if matrix[x][j] == 'T':
            tunels_poss.append(x)
            tunels_poss.append(j)

for x in range(n):
    for j in range(len(matrix)):
        if matrix[x][j] == 'F':
            finish_poss.append(x)
            finish_poss.append(j)

directions = {  # създаваме променлива, в която да пазим посоките
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input()

while command != 'End':
    car_poss = move(command)

    if car_poss == finish_poss:
        km += 10
        matrix[car_poss[0]][car_poss[1]] = 'C'
        print(f"Racing car {racing_number} finished the stage!")
        print(*matrix, sep='\n')
        break

    if matrix[car_poss[0]][car_poss[1]] == '.':
        km += 10
    elif matrix[car_poss[0]][car_poss[1]] == 'T':
        matrix[car_poss[0]][car_poss[1]] = '.'
        km += 30

    command = input()

print(km)

# 5
# 01
# . . . . .
# . . . T .
# . . . . .
# . T . . .
# . . F . .
# down
# right
# right
# right
# down
# right
# up
# down
# right
# up
# End