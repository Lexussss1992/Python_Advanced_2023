import math

even_numbers = []
odd_numbers = []

for i in range(1, int(input()) + 1):
    sum_letters = 0
    for x in input():
        sum_letters += ord(x)
    sum_letters = math.floor(sum_letters / i)
    if sum_letters % 2 == 0:
        even_numbers.append(sum_letters)
    else:
        odd_numbers.append(sum_letters)

if sum(even_numbers) == sum(odd_numbers):
    print(", ".join(str(i) for i in set(even_numbers).union(set(odd_numbers))))
elif sum(odd_numbers) > sum(even_numbers):
    print(", ".join(str(i) for i in set(odd_numbers).difference(set(even_numbers))))
elif sum(even_numbers) > sum(odd_numbers):
    print(", ".join(str(i) for i in set(even_numbers).symmetric_difference(set(odd_numbers))))