a, b, c = int(input()), int(input()), int(input())
sum_positive = 0
for num in [a, b, c]:
    if num > 0:
        sum_positive += num
print(sum_positive)
