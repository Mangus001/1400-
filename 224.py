a, b, c, d = float(input()), float(input()), float(input()), float(input())
count_neg = 0
for num in [a, b, c, d]:
    if num < 0:
        count_neg += 1
print(count_neg)
