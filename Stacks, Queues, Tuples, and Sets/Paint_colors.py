from collections import deque

string = [x for x in input().split()]
main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']
colors = []

while string:
    first_substring = ''
    last_substring = ''
    reversed_color = ''
    if len(string) > 1:
        first_substring = string.pop(0)
        last_substring = string.pop()
        color = first_substring + last_substring
        reversed_color = last_substring + first_substring
    else:
        color = string.pop()

    if color in main_colors:
        colors.append(color)
    elif reversed_color in main_colors:
        colors.append(reversed_color)
    elif color in secondary_colors or reversed_color in secondary_colors:
        if color == 'orange' or reversed_color == 'orange':
            colors.append('orange')
        elif color == 'purple' or reversed_color == 'purple':
            colors.append('purple')
        elif color == 'green' or reversed_color == 'green':
            colors.append('green')
    else:
        if len(first_substring[:-1]) == 0 and len(last_substring[:-1]) == 0:
            continue
        elif len(first_substring[:-1]) == 0 and len(last_substring[:-1]) > 0:
            string.insert(int(len(string)/2), last_substring[:-1])
        elif len(first_substring[:-1]) > 0 and len(last_substring[:-1]) == 0:
            string.insert(int(len(string)/2), first_substring[:-1])
        else:
            string.insert(int(len(string) / 2), first_substring)
            string.insert(int(len(string) / 2 + 1), last_substring)

print(colors)