from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque([x for x in input().split()])
total_nectar = 0

while bees and nectar:
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
            if nectar_value == 0:
                total_nectar += 0
            elif nectar_value != 0:
                total_nectar += abs(bee_collected_nectar / nectar_value)
    else:
        bees.appendleft(bee_collected_nectar)

print(f'Total honey made: {total_nectar}')

if len(bees) > 0 and len(nectar) == 0:
    print(f'Bees left: {", ".join(str(x) for x in bees)}')
elif len(nectar) > 0 and len(bees) == 0:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')
