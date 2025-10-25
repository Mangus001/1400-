a2 = int(input("Введите цифру десятков числа a: "))
a1 = int(input("Введите цифру единиц числа a: "))
b = int(input("Введите однозначное число b: "))

a = 10 * a2 + a1
found = False

for b_candidate in range(10):
    d = a - b_candidate
    if 10 <= d <= 99:
        d2 = d // 10
        d1 = d % 10
        print(f"При b = {b_candidate}: число разности = {d}")
        print(f"Цифры разности: десятки = {d2}, единицы = {d1}")
        found = True

if not found:
    print("Нет подходящего b для получения двузначной разности.")
