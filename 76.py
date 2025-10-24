N = int(input("Введите двузначное число: "))

if N < 10 or N > 99:
    print("Ошибка: число должно быть двузначным (от 10 до 99).")
else:
    tens = N // 10
    units = N % 10
    
    swapped_number = units * 10 + tens
    
    print(f"Число, полученное перестановкой цифр: {swapped_number}")
