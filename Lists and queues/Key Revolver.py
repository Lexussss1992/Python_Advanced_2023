from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
inteL_value = int(input())
count = 0
count_bullets = 0

while len(locks) > 0:
    if inteL_value > 0:
        if len(bullets) > 0:
            if bullets[-1] - locks[0] <= 0:
                print('Bang!')
                bullets.pop()
                locks.popleft()
                count += 1
                count_bullets += 1
                if barrel_size == count and len(bullets) > 0:
                    print('Reloading!')
                    count = 0
            else:
                print('Ping!')
                bullets.pop()
                count += 1
                count_bullets += 1
                if barrel_size == count and len(bullets) > 0:
                    print('Reloading!')
                    count = 0
        else:
            print(f"Couldn't get through. Locks left: {len(locks)}")
            break
else:
    print(f'{len(bullets)} bullets left. Earned ${inteL_value - bullet_price * count_bullets}')