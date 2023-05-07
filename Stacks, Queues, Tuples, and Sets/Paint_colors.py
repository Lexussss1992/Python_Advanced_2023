from collections import deque

string = [x for x in input().split()]
main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']
colors = []

while string:
    first_substring = string.pop(0)
    last_substring = string.pop()
    color = first_substring + last_substring

    if color in main_colors:
        colors.append(color)
    elif color in secondary_colors:
        if color == 'redyellow':
            colors.append('orange')
        elif color == 'redblue':
            colors.append('purple')
        elif color == 'yellowblue':
            colors.append('green')
    else:
        if len(first_substring[:-1]) == 0:
            continue
        else:
            string.append()
        if len(last_substring[:-1]) == 0:
            continue
        else:
            pass
print(colors)