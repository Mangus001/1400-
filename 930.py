arr = [random.randint(1, 100) for _ in range(20)]
max_elem = max(arr)
min_elem = min(arr)
diff = max_elem - min_elem
index_max = arr.index(max_elem)
index_min = arr.index(min_elem)
max_indices = [i for i, v in enumerate(arr) if v == max_elem]
min_indices = [i for i, v in enumerate(arr) if v == min_elem]
print(max_elem, min_elem, diff, index_max, min_indices[0], max_indices[0])
