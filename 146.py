number = int(input())

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

all_same = (hundreds == tens == units)

any_same = (hundreds == tens or hundreds == units or tens == units)

print("Все цифры одинаковые:" , "да" if all_same else "нет")
print("Есть одинаковые цифры:" , "да" if any_same else "нет")
