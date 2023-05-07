from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque([x for x in input().split()])
total_nectar = 0

while bees and nectar and symbols:
    bee_collected_nectar = bees.popleft()
    nectar_value = nectar.pop()

    if nectar_value >= bee_collected_nectar:
        symbol = symbols.popleft()
        if symbol == '+':
            total_nectar += abs(bee_collected_nectar + nectar_value)
        elif symbol == '-':
            total_nectar += abs(bee_collected_nectar - nectar_value)
        elif symbol == '*':
            total_nectar += abs(bee_collected_nectar * nectar_value)
        elif symbol == '/':
            total_nectar += abs(bee_collected_nectar / nectar_value)
    else:
        bees.appendleft(bee_collected_nectar)

print(f'Total honey made: {total_nectar}')

if bees:
    print(f'Bees left: {", ".join([str(x) for x in bees])}')
else:
    print(f'Nectar left: {", ".join([str(x) for x in nectar])}')