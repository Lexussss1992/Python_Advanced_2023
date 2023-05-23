def even_odd_filter(**args):
    for key, value in args.items():
        if key == 'even':
            for x in value:
                return args.values() if x % 2 == 0 else None
        elif key == 'odd':
            for x in value:
                return args.values() if x % 2 != 0 else None


print(even_odd_filter(
odd=[1, 2, 3, 4, 10, 5],
even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))