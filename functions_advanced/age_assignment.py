def age_assignment(*args, **kwargs):
    result = []
    for key, value in sorted(kwargs.items(), key=lambda x: x[0]):
        for x in args:
            for j in x:
                if key == j:
                    result.append(f'{x} is {value} years old.')
    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

# sorted(my_dict.items(), key=lambda x: x[0])