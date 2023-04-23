numbers = input().split()
numbers = [int(x) for x in numbers]
n, m = numbers

set_n = set()
set_m = set()
set_inter = set()

for i in range(n):
    num = int(input())
    set_n.add(num)
for x in range(m):
    num = int(input())
    set_m.add(num)

set_inter = [int(x) for x in set_n.intersection(set_m)]
for x in set_inter:
    print(x)