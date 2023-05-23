def even_odd(*args):
    numbers = []
    if args[-1] == 'even':
        for x in args[0:-1]:
            if x % 2 == 0:
                numbers.append(x)
    elif args[-1] == 'odd':
        for x in args[0:-1]:
            if x % 2 != 0:
                numbers.append(x)
    return numbers


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))