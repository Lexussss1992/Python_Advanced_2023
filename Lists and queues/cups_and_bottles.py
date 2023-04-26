from collections import deque

cups = deque(int(x) for x in input().split())
bottles = deque(int(x) for x in input().split())
wasted_water = 0

while True:
    if bottles[-1] - cups[0] > 0:
        wasted_water += bottles[-1] - cups[0]
        bottles.pop()
        cups.popleft()
    elif bottles[-1] - cups[0] == 0:
        bottles.pop()
        cups.popleft()
    else:
        cups[0] = cups[0] - bottles[-1]
        bottles.pop()
    if len(cups) == 0 or len(bottles) == 0:
        break
    else:
        continue

if len(cups) == 0:
    print("Bottles: ", end="")
    print(*bottles)
    print(f'Wasted litters of water: {wasted_water}')
elif len(bottles) == 0:
    print("Cups: ", end="")
    print(*cups)
    print(f'Wasted litters of water: {wasted_water}')