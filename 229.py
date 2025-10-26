numbers = [int(input()) for _ in range(6)]
sum_positive = 0
for num in numbers:
    if num > 0:
        sum_positive += num
print(sum_positive)
