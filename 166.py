number = int(input("Введите четырехзначное число: "))
b = int(input("Введите цифру b (от 0 до 9): "))

digits = [
    number // 1000,
    (number // 100) % 10,
    (number // 10) % 10,
    number % 10
]

contains_4 = (4 in digits)

contains_b = (b in digits)

print("Цифра 4 входит в число:", "да" if contains_4 else "нет")
print(f"Цифра {b} входит в число:", "да" if contains_b else "нет")
