from collections import deque

seats = input().split(', ')
seq_one = deque([int(x) for x in input().split(', ')])
seq_two = deque([int(x) for x in input().split(', ')])

seat_matches = []
rotations = 0

while len(seat_matches) < 3 and rotations < 10:
    first_number = seq_one.popleft()
    last_number = seq_two.pop()
    letter = chr(first_number + last_number)

    for seat in seats:
        if str(first_number) + letter in seat or str(last_number) + letter in seat:
            seat_matches.append(seat)
            seats.remove(seat)
            break
        else:
            continue
    seq_one.append(first_number)
    seq_two.appendleft(last_number)
    rotations += 1

print(f'Seat matches: {", ".join(i for i in seat_matches)} ')
print(f'Rotations count: {rotations}')

# 17K, 20B, 3C, 15D, 31Z, 28F
# 20, 35, 15, 3, 2, 10
# 1, 15, 64, 53, 45, 46

# 25A, 16B, 44T, 49D, 27M, 44F
# 25, 3, 31, 49, 26, 13
# 10, 15, 44, 40

# 15C, 25C, 36C, 43P, 40E, 38G
# 15, 25, 80, 40, 15, 99, 52
# 15, 42, 29