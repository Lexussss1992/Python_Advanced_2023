st = set()

for _ in range(int(input())):
    first_data, second_data = [i.split(',') for i in input().split('-')]

    first_range = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_range = set(range(int(second_data[0]), int(second_data[1]) + 1))

    intersection = first_range.intersection(second_range)

    if len(st) < len(intersection):
        st = intersection

print(f'Longest intersection is [{", ".join(str(i) for i in st)}] with length {len(st)}')