first_seq = set([int(i) for i in input().split()])
second_seq = set([int(i) for i in input().split()])
n = int(input())

for i in range(n):
    first_command, *data = input().split()

    command = first_command + ' ' + data.pop(0)

    if command == 'Add First':
        [first_seq.add(int(i)) for i in data]
    elif command == 'Add Second':
        [second_seq.add(int(i)) for i in data]
    elif command == 'Remove First':
        [first_seq.discard(int(i)) for i in data]
    elif command == 'Remove Second':
        [second_seq.discard(int(i)) for i in data]
    else:
        if first_seq.issubset(second_seq) or second_seq.issubset(first_seq):
            print(True)
        else:
            print(False)

print(*sorted(first_seq), sep=', ')
print(*sorted(second_seq), sep=', ')