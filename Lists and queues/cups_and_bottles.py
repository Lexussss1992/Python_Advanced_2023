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
    print(f'Bottles: {[]}')
    print(f'Wasted liters of water: {wasted_water}')
elif len(bottles) == 0:
    print(f'Cups: {print(*cups)}')
    print(f'Wasted liters of water: {wasted_water}')