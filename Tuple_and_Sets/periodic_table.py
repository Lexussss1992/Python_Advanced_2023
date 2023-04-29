n = int(input())
elements = tuple(input().split() for i in range(n))
el_list = []
el_set = set()

for i in elements:
    for x in i:
        el_list.append(x)

for i in el_list:
    el_set.add(i)


for i in el_set:
    print(i)