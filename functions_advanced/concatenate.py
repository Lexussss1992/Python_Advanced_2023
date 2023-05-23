def concatenate(*args, **kwargs):
    string = []
    for i in args:
        string.append(i)

    conc_str = ''.join(string)

    for i in conc_str:
        for key, value in kwargs.items():
            if i == key:
                idx = conc_str.index(i)
                conc_str = value
    return conc_str



print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))