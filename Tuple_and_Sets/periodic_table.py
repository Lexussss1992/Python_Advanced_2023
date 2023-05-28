n = int(input())
elements = tuple(input().split() for i in range(n))
print(elements)
el_list = []
[el_list.append(x) for i in elements for x in i]
el_set = set()
var = {el_set.add(i) for i in el_list}

for i in el_set:
    print(i)