from collections import deque

rows, cols = [int(i) for i in input().split()]
snake = deque(input())

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        char = snake.popleft()
        matrix[row].append(char)
        snake.append(char)

for index, item in enumerate(matrix, start=1):
    if index % 2 == 0:
        print(*item[::-1], end='\n', sep='')
    else:
        print(*item, end='\n', sep='')