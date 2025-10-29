import math

def x(y_value):
    return math.sqrt(y_value / 0.4) - 2

x0 = x(0)
x2 = x(2)

area, _ = integrate.quad(lambda x: 0.4 * (x+2)**2, x0, x2)
print(f"Приближенная площадь: {area:.4f}")
