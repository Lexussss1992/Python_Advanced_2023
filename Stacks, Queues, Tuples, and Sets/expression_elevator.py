from collections import deque

expression = input().split()
operators = ['+', '-', '*', '/']
exp_queue = deque()
product = 1

for i in expression:
    if i not in operators:
        exp_queue.append(i)
    else:
        for x in exp_queue:
            if i == '+':
                product += int(exp_queue.popleft())
            elif i == '-':
                product -= int(exp_queue.popleft())
            elif i == '*':
                product *= int(exp_queue.popleft())
            elif i == '/':
                product /= int(exp_queue.popleft())
print(product)