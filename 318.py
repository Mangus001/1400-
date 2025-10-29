sum_result = 0
for i in range(12, 103, 10):
    sign = (-1) ** ((i - 12)//10)
    sum_result += sign * i ** 2

print(f"Результат суммы: {sum_result}")
