from collections import deque

materials = deque([int(i) for i in input().split()])
magic_level = deque([int(i) for i in input().split()])

presents = {
    range(100, 200): 'Gemstone',
    range(200, 300): 'Porcelain Sculpture',
    range(300, 400): 'Gold',
    range(400, 500): 'Diamond Jewellery'
}

gifts = {}

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()
    result = int(material + magic)

    for key, value in presents.items():
        if result in key:
            if value in gifts.keys():
                gifts[value] += 1
                break
            else:
                gifts[value] = 1
        else:
            if result < 100:
                if result % 2 == 0:
                    material *= 2
                    magic *= 3
                    result = int(material + magic)
                else:
                    material *= 2
                    magic *= 2
                    result = int(material + magic)
                if result < 100:
                    break
            elif result > 499:
                result = int(result / 2)
                if result in key:
                    if value in gifts.keys():
                        gifts[value] += 1
                        break
                    else:
                        gifts[value] = 1
            else:
                continue

if ('Gemstone' in gifts and 'Porcelain Sculpture' in gifts) or ('Gold' in gifts and 'Diamond Jewellery' in gifts):
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')


if materials:
    print(f'Materials left: {", ".join(str(i) for i in materials)}')
if magic_level:
    print(f'Magic left: {", ".join(str(i) for i in magic_level)}')


gifts = sorted(gifts.items(), key=lambda x: x[0])

for key, value in gifts:
    print(f'{key}: {value}')

# 105 20 30 25
# 120 60 11 400 10 1

# 30 5 21 6 0 91
# 15 9 5 15 8

# 200
# 5 15 32 20 10 5