k = int(input())

pair_number = (k + 1) // 2

n = 10 + pair_number - 1
tens_digit = n // 10
units_digit = n % 10

if k % 2 == 1:
    digit = tens_digit
else:
    digit = units_digit

print("Номер пары:", pair_number)
print("Двухзначное число:", n)
print("k-я цифра:", digit)
