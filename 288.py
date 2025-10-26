b = int(input("Введите b (1 ≤ b ≤ 10): "))
product = 1
for i in range(1, b + 1):
    product *= i
print(product)
