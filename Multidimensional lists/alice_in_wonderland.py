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
    if command == 'right':
        pass
    elif command == 'left':
        pass
    elif command == 'down':
        pass
    elif command == 'up':
        pass