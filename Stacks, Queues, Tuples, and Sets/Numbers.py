first_seq = set([int(i) for i in input().split()])
second_seq = set([int(i) for i in input().split()])
n = int(input())

myd_dict = {
    'Add first': lambda x: first_seq.add(x),
    'Add second': lambda x: second_seq.add(x),
    'Remove first': lambda x: first_seq.remove(x),
    'Remove second': lambda x: second_seq.remove(x)
}

for _ in range(n):
    data = [x for x in input().split()]
    myd_dict[data[0] + ' ' + data[1]](data[2])
print(first_seq)
print(second_seq)