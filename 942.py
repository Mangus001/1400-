arr = [random.randint(1, 10) for _ in range(20)]
max_elem = max(arr)
min_elem = min(arr)
count_max = sum(1 for x in arr if x == max_elem)
count_min = sum(1 for x in arr if x == min_elem)
print(count_max, count_min)
