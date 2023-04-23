n = int(input())

matrix = []

for i in range(n):
    matrix.append([int(el) for el in input().split(", ")])

sum_pd = 0
sum_sd = 0
nums_pd = []
nums_sd = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            sum_pd += matrix[i][j]
            nums_pd.append(matrix[i][j])

str_nums = [str(num) for num in nums_pd]
print(f"Primary diagonal: {', '.join(str_nums)}. Sum: {sum_pd}")

result = []
sum_result = 0
for index in range(len(matrix)):
    result.append(matrix[index][len(matrix) - 1 - index])
    sum_result += int(matrix[index][len(matrix) - 1 - index])

str_res = [str(el) for el in result]

str_nums = [str(num) for num in nums_sd]
print(f"Secondary diagonal: {', '.join(str_res)}. Sum: {sum_result}")
