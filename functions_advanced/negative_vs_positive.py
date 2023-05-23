numbers = [int(i) for i in input().split()]

sum_negatives = 0
sum_positives = 0

for i in numbers:
    if i < 0:
        sum_negatives += i
    elif i > 0:
        sum_positives += i

print(sum_negatives)
print(sum_positives)

if abs(sum_negatives) > sum_positives:
    print("The negatives are stronger than the positives")
elif sum_positives > abs(sum_negatives):
    print("The positives are stronger than the negatives")