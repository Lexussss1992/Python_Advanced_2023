quantity = int(input())
orders = input().split()
stack_orders = []

for i in range(len(orders)):
    stack_orders.append(int(orders.pop()))

print(max(stack_orders))

for x in range(len(stack_orders)):
    if quantity - stack_orders.pop() >= 0:
        quantity = quantity - stack_orders.pop()

if len(stack_orders) > 0:
    print(f"Orders left: {stack_orders}")
elif len(stack_orders) == 0:
    print("Orders completed")