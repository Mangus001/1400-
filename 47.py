import math

a = float(input("Введите длину основания a: "))
b = float(input("Введите длину основания b: "))
h = float(input("Введите высоту h: "))

half_diff = abs(b - a) / 2

c = math.sqrt(half_diff ** 2 + h ** 2)

perimeter = a + b + 2 * c

print(f"Периметр трапеции: {perimeter:.2f}")
