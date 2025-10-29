x = int(input("x = "))
y = int(input("y = "))

product1 = 0
for _ in range(y):
    product1 += x
print(f"Произведение (способ 1): {product1}")

def multiply(a, b):
    result = 0
    while b > 0:
        if b % 2 == 1:
            result += a
        a += a
        b //= 2
    return result

product2 = multiply(x, y)
print(f"Произведение (способ 2): {product2}")
