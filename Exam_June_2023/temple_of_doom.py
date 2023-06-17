from collections import deque

tools = deque([int(i) for i in input().split()])
substances = deque([int(i) for i in input().split()])
challenges = deque([int(i) for i in input().split()])

while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()
    result = tool * substance

    if len(challenges) <= 0:
        break

    if result in challenges:
        challenges.remove(result)
        continue

    if result not in challenges:
        tool += 1
        tools.append(tool)
        substance -= 1
        if substance <= 0:
            continue
        else:
            substances.append(substance)

if len(challenges) > 0:
    print('Harry is lost in the temple. Oblivion awaits him.')

if len(challenges) == 0:
    print("Harry found an ostracon, which is dated to the 6th century BCE." )

if tools:
    print(f'Tools: ', end='')
    print(*tools, sep=', ')

if substances:
    print(f'Substances: ', end='')
    print(*substances, sep=', ')

if challenges:
    print(f'Challenges: ', end='')
    print(*challenges, sep=', ')

# 2 4 6 8
# 11 3 5 7 9
# 24 28 18 30

# 13 7 4 22 11 15 20
# 3 2 1
# 12 10 5