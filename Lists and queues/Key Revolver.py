from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
inteL_value = int(input())
count = 0

while len(locks) > 0:
    if inteL_value > 0:
        if len(locks) > 0 and len(bullets) > 0:
            if bullets[-1] - locks[0] <= 0:
                print('Bang!')
                locks.popleft()
                bullets.pop()
                count += 1
                if count == barrel_size:
                    print("Reloading!")
                    count = 0
            else:
                print('Ping!')
                bullets.pop()
                count += 1
                if count == barrel_size:
                    print("Reloading!")
                    count = 0
        else:
            break
    else:
        break
