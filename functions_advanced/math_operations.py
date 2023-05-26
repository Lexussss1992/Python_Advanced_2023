def math_operations(*args, **kwargs):
    from collections import deque
    deque_args = deque(i for i in args)
    result = []
    while len(deque_args) > 0:
        for key, value in kwargs.items():
            deq_value = deque_args[0]
            if key == 'a':
                kwargs[key] = deq_value + value
            elif key == 's':
                kwargs[key] = value - deq_value
            elif key == 'd':
                if deq_value != 0:
                    kwargs[key] = value / deq_value
            elif key == 'm':
                kwargs[key] = deq_value * value
            deq_value = deque_args.popleft()
            if len(deque_args) <= 0:
                break
    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sorted_kwargs:
        result.append(f'{key}: {value:.1f}')

    return '\n'.join(result)

# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))

#print(math_operations(6.0, a=0, s=0, d=5, m=0))