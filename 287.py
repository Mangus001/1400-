a = int(input("Введите a (1 ≤ a ≤ 15): "))
product = 1
for i in range(a, 16):
    product *= i
print(product)
