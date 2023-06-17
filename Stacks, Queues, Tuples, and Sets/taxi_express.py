from collections import deque

customers = deque([int(i) for i in input().split(', ')])
taxi = deque([int(i) for i in input().split(', ')])
total_time = 0

while customers and taxi:
    customer = customers.popleft()
    taxi_car = taxi.pop()

    if customer <= taxi_car:
        total_time += customer
    else:
        customers.appendleft(customer)

if len(customers) == 0:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(str(i) for i in customers)}')


# 4, 6, 8, 5, 1
# 1, 9, 15, 10, 6

# 10, 5, 8, 9
# 2, 4, 5, 8

# 2, 8, 4, 3, 11, 7
# 10, 15, 4, 6, 3, 10, 2, 1