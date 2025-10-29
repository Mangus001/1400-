n = int(input("Введите n (2 ≤ n ≤ 10): "))
sum_factorials = 0
for k in range(1, n+1):
    factorial = 1
    for i in range(1, k+1):
        factorial *= i
    sum_factorials += factorial
print(f"Сумма: {sum_factorials}")
