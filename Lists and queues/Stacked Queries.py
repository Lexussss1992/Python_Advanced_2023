number_of_lines = int(input())
stack = []
reversed_stack = []
i = 0

while i < number_of_lines:
    query = input()
    if query == '2' and len(stack) > 0:
        stack.pop()
    elif query == '3' and len(stack) > 0:
        print(max(stack))
    elif query == '4' and len(stack) > 0:
        print(min(stack))
    elif query[0] == '1':
        query = query.split()
        stack.append(int(query[1]))
    i += 1

for i in range(0, len(stack)):
    reversed_stack.append(stack.pop())

print(*reversed_stack, sep=', ')