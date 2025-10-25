a, b, c = float(input()), float(input()), float(input())

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Да")
else:
    print("Нет")
