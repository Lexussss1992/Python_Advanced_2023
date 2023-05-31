with open('text.txt', 'r') as f:
    i = 0
    char_remove = ["-", ",", ".", "!", "?"]
    for line in f.readlines():
        if i % 2 == 0:
            for char in char_remove:
                line = line.replace(char, '@')
                new_line = [i for i in line.split()]
            print(*new_line[::-1])
        i += 1