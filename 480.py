sequence = list(map(int, input().split()))
sum_numbers = 0
count = 0
for num in sequence:
    if num == 0:
        break
    sum_numbers += num
    count += 1
print(sum_numbers)
print(count)
