N = int(input("Введите трехзначное число: "))

if N < 100 or N > 999:
    print("Ошибка: число должно быть трехзначным.")
else:
    units = N % 10
    remaining = N // 10

    new_number = units * 100 + remaining

    print(f"Новое число после перемещения последней справа цифры в начало: {new_number}")
