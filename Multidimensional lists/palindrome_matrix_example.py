INPUT = 3
MATRIX_DIM = (2 * INPUT) + 1

palindorme_matrix = []

current_value = 1
current_row = []
for idx in range(MATRIX_DIM):
    current_row.append(current_value)
    if idx >= INPUT:
        current_value -= 1
    else:
        current_value += 1
palindorme_matrix.append(current_row)

for row in range(1, MATRIX_DIM):
    new_row = current_row.copy()
    for i in range(len(current_row)):
        new_row[i] += 1
        if new_row[i] > (INPUT + 1):
            new_row[i] = 1
    palindorme_matrix.append(new_row)
    current_row = new_row.copy()

print("Palindrome Matrix ", palindorme_matrix)