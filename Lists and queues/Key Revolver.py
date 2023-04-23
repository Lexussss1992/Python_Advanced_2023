from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
inteL_value = int(input())
count = 0

for i in reversed(bullets):
    if inteL_value > 0:
        if count == barrel_size:
            print("Reloading!")
            count = 0
        else:
            if len(locks) > 0:
                if i - locks[0] <= 0:
                    print('Bang!')
                    locks.popleft()
                    count += 1
                else:
                    print('Ping!')
                    count += 1
            else:
                break
    else:
        break
