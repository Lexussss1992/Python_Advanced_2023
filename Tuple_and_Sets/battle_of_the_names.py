even_numbers = set()
odd_numbers = set()

for i in range(1, int(input()) + 1):
    sum_letters = 0
    for x in input():
        sum_letters += ord(x)
    sum_letters = round(sum_letters / i)
    if sum_letters % 2 == 0:
        even_numbers.add(sum_letters)
    else:
        odd_numbers.add(sum_letters)

print(even_numbers)
print(odd_numbers)