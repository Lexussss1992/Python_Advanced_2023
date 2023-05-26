from collections import deque


def math_operations(*args, **kwargs):
    deque_args = deque(i for i in args)
    result = []
    deq_value = deque_args.popleft()
    while deque_args:
        for key, value in kwargs.items():
            if key == 'a':
                result.append([deq_value + value])
            elif key == 's':
                result.append([deq_value - value])
            elif key == 'd':
                if deque_args.popleft() != 0:
                    result.append([deq_value / value])
            elif key == 'm':
                result.append([deq_value * value])
            deq_value = deque_args.popleft()

    return result, deque_args

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))