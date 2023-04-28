number_of_sets = [int(i) for i in input().split()]
n = number_of_sets[0]
m = number_of_sets[1]
lst1 = []
lst2 = []

for i in range(n + m):
    number = input()
    if i < n:
        lst1.append(number)
    else:
        lst2.append(number)

set1 = set(lst1)
set2 = set(lst2)
intersection = set1 & set2
for i in intersection:
    print(i)