use_input = input().split('|')

for i in range(len(use_input) - 1, -1, -1):
    # print(use_input[i].split(' '), end=' ')
    [print(x, end=' ') if x != '' else '' for x in use_input[i].split(' ')]