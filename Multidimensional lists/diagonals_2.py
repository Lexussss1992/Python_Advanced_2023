n = int(input())
matrix = []
primary_diagonal = 0
secondary_diagonal = 0
# for i in range(n):
#     matrix.append([])
#     for j in range(1, n + 1):
#         matrix[i].append(j + (i * 3))

for row in range(n):
    lines = [int(x) for x in input().split(', ')]
    matrix.append(lines)

# sum_diagonal = sum(matrix[n - i - 1][n - i - 1] for i in range(n))

for i in range(n):
    primary_diagonal += matrix[n - i - 1][n - i - 1]
    secondary_diagonal += matrix[i][n - i - 1]

prime_diagonal = [matrix[n - i - 1][n - i - 1] for i in range(n)]
sec_diagonal = [matrix[i][n - i - 1] for i in range(n)]

print(f'Primary diagonal: {", ".join([str(x) for  x in prime_diagonal[::-1]])}. Sum: {primary_diagonal}')
print(f'Secondary diagonal: {", ".join([str(x) for  x in sec_diagonal])}. Sum: {secondary_diagonal}')