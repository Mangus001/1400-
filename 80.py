N = int(input("Введите трехзначное число: "))

if N < 100 or N > 999:
    print("Ошибка: число должно быть трехзначным.")
else:
    hundreds = N // 100
    remaining = N % 100
    
    new_number = remaining * 10 + hundreds
    
    print(f"Новое число после перемещения первой слева цифры: {new_number}")
