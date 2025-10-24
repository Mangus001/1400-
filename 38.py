import math
a = float(input("Введите длину верхнего основания a: "))
b = float(input("Введите длину нижнего основания b: "))
h = float(input("Введите высоту h: "))

half_diff = abs(b - a) / 2
c = math.sqrt(half_diff ** 2 + h ** 2)

perimeter = a + b + 2 * c

print(f"Периметр трапеции: {perimeter:.2f}")
