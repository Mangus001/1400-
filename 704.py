data = [list(map(float, input().split())) for _ in range(12)]
max_salary = max(max(row) for row in data)
worker_max_sum = max(sum(row) for row in data)
month_sums = [sum(col) for col in zip(*data)]
max_month_sum = max(month_sums)
print(max_salary)
print(worker_max_sum)
print(month_sums.index(max_month_sum)+1)
