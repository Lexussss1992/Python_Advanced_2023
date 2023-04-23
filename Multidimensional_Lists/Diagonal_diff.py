n = int(input())

matrix = []

for i in range(n):
    matrix.append([int(num) for num in input().split()])

#Primary diagonal
sum_pd = 0
nums_pd = []

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if row == col:
            nums_pd.append(matrix[row][col])
            sum_pd += matrix[row][col]

str_nums_pd = [str(num) for num in nums_pd]

sum_sd = 0
nums_sd = []

for row in range(len(matrix)):
    nums_sd.append(matrix[row][len(matrix) - 1 - row])
    sum_sd += int(matrix[row][len(matrix) - 1 - row])
str_nums_sd = [str(num) for num in nums_sd]

diff = abs(sum_pd - sum_sd)
print(f"{diff}")