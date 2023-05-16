rows = int(input())
matrix = []

for i in range(rows):
    matrix.append([x for x in input().split()])
print(matrix)