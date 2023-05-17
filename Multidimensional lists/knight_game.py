n = int(input())
matrix = [input().split() for x in range(n)]
k_matrix = []

for x in matrix:
    k_matrix.append(*x)

for i in range(len(k_matrix)):
    for x in k_matrix[i]:
        print(x)

print(k_matrix)
print(matrix)