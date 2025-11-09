count = 0
for num in range(100, 501):
    s = sum(int(digit) for digit in str(num))
    if s == 15:
        count += 1
print(count)
