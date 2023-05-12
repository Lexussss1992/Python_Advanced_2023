from collections import deque

rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for u in range(rows)]
user_input = deque([x for x in input().split()])

while user_input != 'END':
    command, coordinates = user_input.popleft(), [int(x) for x in user_input]
    print(command)
    print(coordinates)
    user_input = deque([x for x in input().split()])

# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END