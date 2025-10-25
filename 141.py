number = int(input())
a = int(input())

first_digit = number // 10
second_digit = number % 10

sum_digits = first_digit + second_digit


multiple_of_3 = (sum_digits % 3 == 0)

if sum_digits != 0:
    multiple_of_a = (a % sum_digits == 0)
else:
    multiple_of_a = False 

print("Сумма цифр кратна 3:", "да" if multiple_of_3 else "нет")
print("Кратна ли сумма цифр числу a:", "да" if multiple_of_a else "нет")
