from collections import deque

chocolate = [int(x) for x in input().split(',')]
milk_cups = deque([int(i) for i in input().split(',')])
milkshakes = 0

while True:
    if len(chocolate) > 0 and len(milk_cups) > 0:
        result = chocolate[-1] - milk_cups[0]

        if result == 0:
            chocolate.pop()
            milk_cups.popleft()
            milkshakes += 1
        else:
            if chocolate[-1] <= 0:
                chocolate.pop()
            elif milk_cups[0] <= 0:
                milk_cups.append(milk_cups[0])
                milk_cups.popleft()
                chocolate[-1] -= 5
    elif milkshakes == 5:
        break
    else:
        break
print(chocolate)
print(milk_cups)