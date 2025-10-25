number = int(input())

first_digit = number // 10
second_digit = number % 10

if first_digit > second_digit:
    print("Первая цифра больше второй")
elif first_digit < second_digit:
    print("Вторая цифра больше первой")
else:
    print("Цифры равны")
