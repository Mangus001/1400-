students = [list(map(int, input().split())) for _ in range(11)]
min_total = min(sum(row) for row in students)
print(min_total)
min_parallels = min(sum(row) for row in zip(*students))
print(min_parallels)
total_per_parallel = [sum(row) for row in zip(*students)]
print(min(total_per_parallel))
