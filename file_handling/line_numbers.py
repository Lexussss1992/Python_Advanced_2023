from string import punctuation

with open('text.txt', 'r') as f:
    i = 1
    for line in f.readlines():
        char = ''.join(char for char in line if char not in punctuation and char != ' ' and char != '\n')
        punctuations = ''.join(char for char in line if char in punctuation)
        output = f'Line {i}: {line}({len(char)})({len(punctuations)})'
        i += 1
        with open('output.txt', 'a') as of:
            of.writelines(output + '\n')