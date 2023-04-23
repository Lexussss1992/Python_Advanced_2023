integer = int(input())
stack = []
strings = []
while integer:
    query = input()
    integer -= 1
    if query == "2":
        if len(stack) > 0:
            stack.pop()
        else:
            continue
    elif query == "3":
        print(max(stack))
    elif query == "4":
        print(min(stack))
    else:
        command, num = query.split()
        if int(command) == 1:
            stack.append(int(num))
for x in stack:
    x = str(x)
    strings.append(x)
print(", ".join(strings[::-1]))