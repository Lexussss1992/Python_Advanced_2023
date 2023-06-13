from collections import deque

bomb_effects = deque([int(i) for i in input().split(', ')])
bomb_casing = deque([int(i) for i in input().split(', ')])

bombs = {
    'Datura bombs': [40, 0],
    'Cherry bombs': [60, 0],
    'Smoke Decoy Bombs': [120, 0]
}

while bomb_casing and bomb_effects:
    bomb_eff = bomb_effects.popleft()
    bomb_case = bomb_casing[-1]
    sum_bomb = bomb_eff + bomb_case
    counter = 0

    for key, value in bombs.items():
        if sum_bomb == value[0]:
            value[1] += 1
            counter += 1
            bomb_casing.pop()

    if counter == 0:
        bomb_casing[-1] -= 5

print(bombs)

if all(value[1] != 0 for value in bombs.values()):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {' '.join(str(bomb) for bomb in bomb_effects)}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {' '.join(str(bomb) for bomb in bomb_casing)}")
else:
    print("Bomb Casings: empty")



# 5, 25, 25, 115
# 5, 15, 25, 35

# 30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
# 20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10