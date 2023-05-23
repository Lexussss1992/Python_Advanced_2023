def even_odd_filter(**kwargs):
    dict = {}
    for key, value in kwargs.items():
        if key == 'even':
            dict[key] = []
            for i in value:
                if i % 2 == 0:
                    dict[key].append(i)
        elif key == 'odd':
            dict[key] = []
            for i in value:
                if i % 2 != 0:
                    dict[key].append(i)
    sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: -len(item[1]))}
    return sorted_dict


print(even_odd_filter(
odd=[1, 2, 3, 4, 10, 5],
even=[3, 4, 5, 7, 10, 2, 5, 5, 2]
))

# odd_result = {key: [idx for idx in val if not idx % 2]
#               for key, val in kwargs.items()}
# even_result = {key: [idx for idx in val if not idx == 2]
#                for key, val in kwargs.items()}
# return odd_result, even_result
