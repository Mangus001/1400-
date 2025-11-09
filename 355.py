count = 0
for num in range(100, 1000):
    if num % 7 == 0:
        s = sum(int(digit) for digit in str(num))
        if s % 7 == 0:
            count += 1
print(count)
