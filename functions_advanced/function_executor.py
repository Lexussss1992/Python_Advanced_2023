def func_executor(*func):
    result = []
    for key, value in func:
        result.append(f"{key.__name__} - {key(*value)}")

    return '\n'.join(result)


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor( (make_upper, ("Python", "softUni")), (make_lower, ("PyThOn",)), ))