arr = [random.randint(1, 10) for _ in range(20)]
min_val = min(arr)
max_val = max(arr)
min_indices = [i for i, v in enumerate(arr) if v == min_val]
max_indices = [i for i, v in enumerate(arr) if v == max_val]
print(min_indices, max_indices)
