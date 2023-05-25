def age_assignment(*args, **kwargs):
    result = []
    for key, value in kwargs.items():
        for x in args[0]:
            if key == x:
                result.append(args[0])
                result.append(value)
    return result


print(age_assignment("Peter", "George", G=26, P=19))