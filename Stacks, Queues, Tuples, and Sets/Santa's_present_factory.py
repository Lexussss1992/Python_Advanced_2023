from collections import deque

material_boxes = deque([int(x) for x in input().split()])
magic_values = deque([int(i) for i in input().split()])

info = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

presents = []

pair_one = ['Doll', 'Wooden train']
pair_two = ['Teddy bear', 'Bicycle']

while material_boxes and magic_values:
    last_box = material_boxes.pop()
    first_magic_value = magic_values.popleft()
    result = last_box * first_magic_value

    if len(presents) >= 2:
        if presents[-2] == 'Doll' and presents[-1] == 'Wooden train':
            break
        elif presents[-2] == 'Teddy bear' and presents[-1] == 'Bicycle':
            break

    if result in info:
        presents.append(info.get(result))
    elif result < 0:
        material_boxes.append(last_box + first_magic_value)
    elif result > 0:
        material_boxes.append(last_box + 15)
    elif last_box == 0 and first_magic_value == 0:
        continue
    elif last_box == 0:
        magic_values.appendleft(first_magic_value)
    elif first_magic_value == 0:
        material_boxes.append(last_box)

if presents:
    print('The presents are crafted! Merry Christmas!')
    print(f'Materials left: {", ".join([str(x) for x in material_boxes] if material_boxes else None)}')
    print(", ".join([str(x) for x in magic_values] if material_boxes else None))
else:
    print('No presents this Christmas!')
    print(f'Materials left: {", ".join([str(x) for x in material_boxes if len(material_boxes) > 0])}')
    print(f'Magic left: {", ".join([str(x) for x in magic_values if len(magic_values) > 0])}')