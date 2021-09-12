integers = [int(x) for x in input().split()]

stack = []

while integers:
    stack.append(integers.pop())

print(" ".join([str(x) for x in stack]))