from collections import deque
from functools import reduce

expression = input().split()
operators = ['+', '-', '*', '/']
exp_queue = []

for i in expression:
    if i not in operators:
        exp_queue.append(int(i))
    elif i == '-':
        result = int(reduce(lambda x, y: x - y, exp_queue))
        exp_queue = []
        exp_queue.append(result)
    elif i == '*':
        result = int(reduce(lambda x, y: x * y, exp_queue))
        exp_queue = []
        exp_queue.append(result)
    elif i == '/':
        result = int(reduce(lambda x, y: x / y, exp_queue))
        exp_queue = []
        exp_queue.append(result)
    elif i == '+':
        result = int(reduce(lambda x, y: x + y, exp_queue))
        exp_queue = []
        exp_queue.append(result)
print(int(*exp_queue))