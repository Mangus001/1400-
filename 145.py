number = int(input())
a = int(input())

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

sum_digits = hundreds + tens + units

product_digits = hundreds * tens * units

is_two_digit_sum = (10 <= sum_digits <= 99)

is_three_digit_product = (100 <= product_digits <= 999)

is_number_greater_than_product = (number > product_digits)

multiple_of_5 = (sum_digits % 5 == 0)

if sum_digits != 0:
    multiple_of_a = (a % sum_digits == 0)
else:
    multiple_of_a = False 

print("Сумма цифр двузначное число:", "да" if is_two_digit_sum else "нет")
print("Произведение цифр трехзначное число:", "да" if is_three_digit_product else "нет")
print("Число больше произведения цифр:", "да" if is_number_greater_than_product else "нет")
print("Кратна ли сумма цифр 5:", "да" if multiple_of_5 else "нет")
print("Кратна ли сумма цифр числу a:", "да" if multiple_of_a else "нет")
