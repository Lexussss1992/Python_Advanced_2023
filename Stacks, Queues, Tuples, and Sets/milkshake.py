from collections import deque

chocolate = deque([int(x) for x in input().split(', ')])
milk_cups = deque([int(i) for i in input().split(', ')])
milkshakes = 0

while True:
    if milkshakes < 5:
        if len(chocolate) > 0 and len(milk_cups) > 0:
            result = chocolate[-1] - milk_cups[0]

            if result == 0:
                chocolate.pop()
                milk_cups.popleft()
                milkshakes += 1
            elif chocolate[-1] > 0 and milk_cups[0] > 0:
                milk_cups.append(milk_cups[0])
                milk_cups.popleft()
                chocolate[-1] -= 5
            elif chocolate[-1] <= 0 and milk_cups[0] <= 0:
                chocolate.pop()
                milk_cups.popleft()
            elif chocolate[-1] <= 0 or milk_cups[0] <= 0:
                if chocolate[-1] <= 0:
                    chocolate.pop()
                elif milk_cups[0] <= 0:
                    milk_cups.popleft()
        else:
            print('Not enough milkshakes.')
            if len(chocolate) == 0 and len(milk_cups) == 0:
                print('Chocolate: empty')
                print('Milk: empty')
            elif len(chocolate) == 0 and len(milk_cups) > 0:
                print('Chocolate: empty')
                print(f'Milk: {", ".join([str(i) for i in milk_cups])}')
            elif len(milk_cups) == 0 and len(chocolate) > 0:
                print(f'Chocolate: {", ".join([str(i) for i in chocolate])}')
                print('Milk: empty')
            break
    else:
        print('Great! You made all the chocolate milkshakes needed!')
        if len(chocolate) == 0:
            print('Chocolate: empty')
            print(f'Milk: {", ".join([str(i) for i in milk_cups])}')
        elif len(milk_cups) == 0:
            print(f'Chocolate: {", ".join([str(i) for i in chocolate])}')
            print('Milk: empty')
        else:
            print(f'Chocolate: {", ".join([str(i) for i in chocolate])}')
            print(f'Milk: {", ".join([str(i) for i in milk_cups])}')
        break

