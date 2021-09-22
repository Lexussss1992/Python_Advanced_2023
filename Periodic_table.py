n = int(input())

set_compounds = set()

for i in range(n):
    compound = input().split()
    for x in range(len(compound)):
        set_compounds.add(compound[x])

for x in set_compounds:
    print(x)