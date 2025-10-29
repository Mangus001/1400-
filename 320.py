import scipy.integrate as integrate

def y(x):
    return 0.3 * (x - 1) ** 2

x1 = 1 + math.sqrt(2/0.3)
x2 = 1 + math.sqrt(4/0.3)

area, _ = integrate.quad(y, x1, x2)
print(f"Приближенная площадь: {area:.4f}")
