from collections import deque


def math_operations(*args, **kwargs):
    deque_args = deque(i for i in args)
    result = [0, 0, 0, 0]
    while len(deque_args) > 0:
        for key, value in kwargs.items():
            deq_value = deque_args[0]
            if key == 'a':
                result[0] = deq_value + value
                kwargs[key] = result[0]
            elif key == 's':
                result[1] = value - deq_value
                kwargs[key] = result[1]
            elif key == 'd':
                if deq_value != 0:
                    result[2] = value / deq_value
                    kwargs[key] = result[1]
            elif key == 'm':
                result[3] = deq_value * value
                kwargs[key] = result[3]
            deq_value = deque_args.popleft()
            if len(deque_args) <= 0:
                break

    return result, deque_args

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))