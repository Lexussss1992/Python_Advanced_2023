def start_spring(**kwargs):
    dict = {}
    ls = []

    for key, value in kwargs.items():
        if value not in dict:
            dict[value] = []
            dict[value].append(key)
        else:
            dict[value].append(key)

    for key in dict:
        dict[key] = sorted(dict[key])

    sorted_dict = sorted(dict.items(), key=lambda item: (-len(item[1]), item[0]))

    for key, value in sorted_dict:
        ls.append(f'{key}:')
        for i in value:
            ls.append(f'-{i}')

    return '\n'.join(i for i in ls)


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect",}

print(start_spring(**example_objects))