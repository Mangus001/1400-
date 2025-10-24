N = int(input("Введите трехзначное число: "))

if N < 100 or N > 999:
    print("Ошибка: число должно быть трехзначным.")
else:
    hundreds = N // 100
    tens = (N // 10) % 10
    units = N % 10
    
    reversed_number = units * 100 + tens * 10 + hundreds
    
    print(f"Число, прочитанное справа налево: {reversed_number}")
