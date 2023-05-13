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
    print(*item, end='\n')