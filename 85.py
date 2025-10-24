N = int(input("Введите четырехзначное число: "))

if 1000 <= N <= 9999:
    thousands = N // 1000
    hundreds = (N // 100) % 10
    tens = (N // 10) % 10
    units = N % 10
    
    sum_digits = thousands + hundreds + tens + units
    print("Сумма цифр:", sum_digits)
else:
    print("Ошибка: число должно быть четырехзначным.")
