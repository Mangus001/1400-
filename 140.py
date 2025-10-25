number = int(input())

first_digit = number // 10
second_digit = number % 10

sum_digits = first_digit + second_digit

is_two_digit_sum = (10 <= sum_digits <= 99)

is_number_greater = (number > sum_digits)

print("Сумма цифр двузначное число:", "да" if is_two_digit_sum else "нет")
print("Число больше суммы его цифр:", "да" if is_number_greater else "нет")
