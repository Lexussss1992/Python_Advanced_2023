n = int(input())
matrix = []
primary_diagonal = 0
secondary_diagonal = 0

for row in range(n):
    lines = [int(x) for x in input().split()]
    matrix.append(lines)

for i in range(n):
    primary_diagonal += matrix[n - i - 1][n - i - 1]
    secondary_diagonal += matrix[i][n - i - 1]

diff = abs(primary_diagonal - secondary_diagonal)

print(diff)