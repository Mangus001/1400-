import math

def f(x):
    return math.asin(x)

a = 0
b = 1 

n = 1000  
h = (b - a) / n

area = 0.5 * (f(a) + f(b))
for i in range(1, n):
    x = a + i * h
    area += f(x)

area *= h
print(f"Приближенная площадь арки: {area}")
