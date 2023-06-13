from collections import deque

bomb_effects = deque([int(i) for i in input().split(', ')])
bomb_casing = deque([int(i) for i in input().split(', ')])

bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}

flag = True

while flag and bomb_casing and bomb_effects:
    bomb_eff = bomb_effects.popleft()
    bomb_case = bomb_casing.pop()
    sum_bomb = bomb_eff + bomb_case

    for bomb, quantity in (('Datura Bombs', 40), ('Cherry Bombs', 60), ('Smoke Decoy Bombs', 120)):
        if sum_bomb == quantity:
            bombs[bomb] += 1
            break
    else:
        bomb_casing.append(bomb_case - 5)
        bomb_effects.appendleft(bomb_eff)
        continue

    if all(value >= 3 for value in bombs.values()):
        flag = False


if not flag:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(bomb) for bomb in bomb_effects)}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join(str(bomb) for bomb in bomb_casing)}")
else:
    print("Bomb Casings: empty")

sorted_bombs = sorted(bombs.items(), key=lambda x: x[0])

for key, value in sorted_bombs:
    print(f'{key}: {value}')


# 5, 25, 25, 115
# 5, 15, 25, 35

# 30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
# 20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10