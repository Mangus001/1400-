number = int(input())

tens = number // 10
units = number % 10

contains_3 = (tens == 3 or units == 3)

a = int(input("Введите цифру a: "))
contains_a = (tens == a or units == a)

print("Цифра 3 входит в число:", "да" if contains_3 else "нет")
print(f"Цифра {a} входит в число:", "да" if contains_a else "нет")
