import math

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
abs_a = abs(a)
abs_b = abs(b)
arith_mean = (abs_a + abs_b) / 2

geom_mean = math.sqrt(abs_a * abs_b)

print(f"Среднее арифметическое модулей: {arith_mean}")
print(f"Среднее геометрическое модулей: {geom_mean}")
