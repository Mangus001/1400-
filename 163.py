number = int(input("Введите трехзначное число: "))
n = int(input("Введите цифру n (от 0 до 9): "))

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

contains_6 = (hundreds == 6 or tens == 6 or units == 6)

contains_n = (hundreds == n or tens == n or units == n)

print("Цифра 6 входит в число:", "да" if contains_6 else "нет")
print(f"Цифра {n} входит в число:", "да" if contains_n else "нет")
