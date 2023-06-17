def numbers_searching(*lst):
    lst = sorted(lst)
    seen = set()
    uniq = []
    for i in lst:
        if i not in uniq:
            uniq.append(i)
        else:
            seen.add(i)

    missing_numbers = []

    for i in range(len(uniq) - 1):
        if uniq[i] + 1 in uniq:
            continue
        else:
            missing_numbers.append(uniq[i] + 1)

    seen = sorted(seen)
    result = []
    result.append(*missing_numbers)
    result.append(seen)

    return result

# print(numbers_searching(1, 2, 4, 2, 5, 4))

# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
