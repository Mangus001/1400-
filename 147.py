number = int(input())
a = int(input()) 

digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10

sum_first_two = digit1 + digit2
sum_last_two = digit3 + digit4
condition_a = (sum_first_two == sum_last_two)

sum_digits = digit1 + digit2 + digit3 + digit4
condition_b = (sum_digits % 3 == 0)

product_digits = digit1 * digit2 * digit3 * digit4
condition_v = (product_digits % 4 == 0)

if product_digits != 0:
    condition_g = (a % product_digits == 0)
else:
    condition_g = False

print("Сумма двух первых равна сумме двух последних:", "да" if condition_a else "нет")
print("Сумма цифр кратна 3:", "да" if condition_b else "нет")
print("Произведение цифр кратно 4:", "да" if condition_v else "нет")
print("Произведение цифр кратно числу a:", "да" if condition_g else "нет")
