a, b, c = float(input()), float(input()), float(input())

if (a + b > c) and (a + c > b) and (b + c > a):
    sides = sorted([a, b, c])
    if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9:
        print("Да")
    else:
        print("Нет")
else:
    print("Нет")
