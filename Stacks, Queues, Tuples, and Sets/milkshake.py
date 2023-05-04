from collections import deque

chocolate = [int(x) for x in input().split(',')]
milk_cups = deque([int(i) for i in input().split(',')])
n = 5

for i in range(n):
    if len(chocolate) > 0  or len(milk_cups) > 0:
        result = chocolate[-1] - milk_cups[0]

        if result == 0:
            chocolate.pop()
            milk_cups.popleft()
        else:
            milk_cups.append(milk_cups[0])
            milk_cups.popleft()
            chocolate.pop()
print(chocolate)
print(milk_cups)