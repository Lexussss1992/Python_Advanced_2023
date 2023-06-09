from collections import deque

mg_coffeine = deque([int(x) for x in input().split(', ')])
energy_drinks = deque([int(x) for x in input().split(', ')])
MAX_CAFFEINE = 300
stamat_caffeine = 0

while mg_coffeine and energy_drinks:
    mg = mg_coffeine.pop()
    drink = energy_drinks[0]
    result = mg * drink

    if result + stamat_caffeine <= MAX_CAFFEINE:
        energy_drinks.popleft()
        stamat_caffeine += result
        continue
    else:
        energy_drinks.popleft()
        energy_drinks.append(drink)
        stamat_caffeine -= 30

    if stamat_caffeine < 0:
        stamat_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")



# 1, 23, 2, 1, 42, 22, 7, 14
# 51, 100, 3, 7