num = int(input())

digits = [int(d) for d in str(num)]
sum_digits = sum(digits)
count_digits = len(digits)
product_digits = 1
sum_squares = 0
sum_cubes = 0
sum_digits_gt_5 = 0

for d in digits:
    product_digits *= d
    sum_squares += d ** 2
    sum_cubes += d ** 3
    if d > 5:
        sum_digits_gt_5 += d

first_digit = int(str(num)[0])
last_digit = int(str(num)[-1])

print("Цифры:", digits)
print("Сумма:", sum_digits)
print("Количество:", count_digits)
print("Произведение:", product_digits)
print("Среднее:", sum_digits / count_digits if count_digits else 0)
print("Сумма квадратов:", sum_squares)
print("Сумма кубов:", sum_cubes)
print("Первая цифра:", first_digit)
print("Сумма первой и последней цифр:", first_digit + last_digit)
