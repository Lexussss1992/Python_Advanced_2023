n = int(input())
matrix = [input().split() for x in range(n)]
k_matrix = []

for el in range(len(matrix)):
    for x in matrix[el]:
        for i in x:
            if i == 'K':
                k_matrix.append(el)
                k_matrix.append(x)


print(k_matrix)
print(matrix)