from collections import deque

material_boxes = deque([int(x) for x in input().split()])
magic_values = deque([int(i) for i in input().split()])

info = {
    150: ['Doll', 0],
    250: ['Wooden train', 0],
    300: ['Teddy bear', 0],
    400: ['Bicycle', 0]
}

presents = []

while material_boxes and magic_values:
    last_box = material_boxes.pop() if magic_values[0] or not material_boxes[0] else 0
    first_magic_value = magic_values.popleft() if last_box or not magic_values[0] else 0

    if not magic_values:
        continue

    result = last_box * first_magic_value

    if result in info:
        presents.append(info.get(result)[0])
    elif result < 0:
        material_boxes.append(last_box + first_magic_value)
    elif result > 0:
        material_boxes.append(last_box + 15)

for key, value in info.items():
    if value in presents:
        value[1] += 1

if 'Doll' in presents and 'Wooden train' in presents:
    print('The presents are crafted! Merry Christmas!')
elif 'Teddy bear' in presents and 'Bicycle' in presents:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if material_boxes and magic_values:
    print(f'Materials left: {", ".join([str(x) for x in material_boxes][::-1])}')
    print(f'Magic left: {", ".join(str(x) for x in magic_values)}')
elif not material_boxes:
    print(f'Magic left: {", ".join(str(x) for x in magic_values)}')
elif not magic_values:
    print(f'Materials left: {", ".join([str(x) for x in material_boxes][::-1])}')

[print(f'{toy}: {presents.count(toy)}') for toy in sorted(set(presents))]
