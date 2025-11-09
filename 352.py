total = 0
for num in range(31, 100):
    last_digit = num % 10
    if num % 3 == 0 and last_digit in [2, 4, 8]:
        total += num
print(f"Сумма: {total}")
