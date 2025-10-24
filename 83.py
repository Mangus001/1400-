N = int(input("Введите трехзначное число: "))

if N < 100 or N > 999:
    print("Ошибка: число должно быть трехзначным.")
else:
    hundreds = N // 100
    tens = (N // 10) % 10
    units = N % 10

    new_number = hundreds * 100 + units * 10 + tens

    print(f"Число после перестановки второй и третьей цифр: {new_number}")
