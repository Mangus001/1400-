n = int(input())
digits = [int(d) for d in str(n)]
max_digit = min_digit = digits[0]
for d in digits:
    if d > max_digit:
        max_digit = d
    if d < min_digit:
        min_digit = d
if (max_digit - min_digit) % 2 == 0:
    print("Да")
else:
    print("Нет")
