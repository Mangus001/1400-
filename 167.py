number = int(input("Введите четырехзначное число: "))

digits = [
    number // 1000,
    (number // 100) % 10,
    (number // 10) % 10,
    number % 10
]

contains_2_or_7 = (2 in digits) or (7 in digits)

contains_3_6_9 = (3 in digits) or (6 in digits) or (9 in digits)

print("Цифры 2 или 7 входят в число:", "да" if contains_2_or_7 else "нет")
print("Цифры 3, 6 или 9 входят в число:", "да" if contains_3_6_9 else "нет")
