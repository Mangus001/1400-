a = int(input("Введите неотрицательное число a: "))
b = int(input("Введите положительное число b: "))
c = int(input("Введите число c: "))
d = int(input("Введите число d: "))

if a < 0:
    print("Число a должно быть неотрицательным.")
elif b <= 0:
    print("Число b должно быть положительным.")
else:
    remainder = a % b
    if remainder == c or remainder == d:
        print("Верно, остаток равен одному из чисел c или d.")
    else:
        print("Неверно, остаток не равен ни c, ни d.")
