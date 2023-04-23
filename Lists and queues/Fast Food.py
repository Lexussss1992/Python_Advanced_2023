from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split(' ')))
print(max(orders))

while food_quantity > 0 or len(orders) > 0:
    if food_quantity - orders[0] >= 0:
        food_quantity = food_quantity - orders[0]
        orders.popleft()
        if len(orders) > 0:
            continue
        else:
            print('Orders complete')
            break
    elif food_quantity - orders[0] <= 0:
        print('Orders left:', end=' ')
        print(*orders, sep=" ")
        break