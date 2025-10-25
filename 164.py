number = int(input("Введите трехзначное число: "))

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

contains_6 = (hundreds == 6 or tens == 6 or units == 6)

print("Цифра 6 входит в число:", "да" if contains_6 else "нет")
