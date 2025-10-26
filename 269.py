import math

p0 = 1.29
z = 1.25e-4
for h in range(0, 1100, 100):
    p = p0 * math.exp(-z * h)
    print(f"Высота: {h} м, плотность: {p:.4f} кг/м^3")
