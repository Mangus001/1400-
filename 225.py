a, b, c, d = int(input()), int(input()), int(input()), int(input())
count_even = 0
for num in [a, b, c, d]:
    if num % 2 == 0:
        count_even += 1
print(count_even)
