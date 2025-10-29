n = int(input("Введите n (1 < n ≤ 10): "))

total = 0
for i in range(1, n + 1):
    sum_odd = 0
    for j in range(1, 2*i, 2):
        sum_odd += j
    total += sum_odd

print(f"Сумма квадратов: {total}")
