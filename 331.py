n = int(input("Введите натуральное число n: "))
sum_odd = 0
for k in range(n):
    sum_odd += 2 * n - 1 + 2 * k
print(f"{n} в кубе равно {sum_odd}")
