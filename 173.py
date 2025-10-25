a = float(input("Введите число a (не равно 0): "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

discriminant = b**2 - 4 * a * c

if discriminant > 0:
    sqrt_D = discriminant**0.5
    x1 = (-b + sqrt_D) / (2 * a)
    x2 = (-b - sqrt_D) / (2 * a)
    print(f"Два различных корня: x1 = {x1}, x2 = {x2}")
elif discriminant == 0:
    x = -b / (2 * a)
    print(f"Одиночный корень: x = {x}")
else:
    print("Решений в действительных числах нет.")
