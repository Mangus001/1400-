a = int(input("Введите a: "))
b = int(input("Введите b (b ≥ a): "))
product = 1
for i in range(a, b + 1):
    product *= i
print(product)
