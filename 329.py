n = int(input("Введите натуральное число n: "))

sum_odd = 0
for i in range(1, 2*n, 2):
    sum_odd += i

print(f"{n} в квадрате равно {sum_odd}")
