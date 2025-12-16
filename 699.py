data = [list(map(float, input().split())) for _ in range(12)]
total_sum = sum(sum(row) for row in data)
per_worker = [sum(row) for row in data]
per_month = [sum(col) for col in zip(*data)]
print(total_sum)
print(per_worker)
print(per_month)
