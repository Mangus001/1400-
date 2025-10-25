
a2 = int(input("Введите цифру десятков первого числа (a2): "))
a1 = int(input("Введите цифру единиц первого числа (a1): "))
b2 = int(input("Введите цифру десятков второго числа (b2): "))
b1 = int(input("Введите цифру единиц второго числа (b1): "))

a = 10 * a2 + a1
b = 10 * b2 + b1

found = False
for a2_candidate in range(1, 10): 
    for a1_candidate in range(0, 10):
        a_candidate = 10 * a2_candidate + a1_candidate
        for b2_candidate in range(1, 10):
            for b1_candidate in range(0, 10):
                b_candidate = 10 * b2_candidate + b1_candidate
                d = a_candidate - b_candidate
                if 10 <= d <= 99:
                    d2 = d // 10
                    d1 = d % 10
                    print(f"Для a = {a_candidate} и b = {b_candidate}:")
                    print(f"Разность d = {d}")
                    print(f"Цифры разности: десятки = {d2}, единицы = {d1}\n")
                    found = True

if not found:
    print("Подходящих разностей не найдено.")
