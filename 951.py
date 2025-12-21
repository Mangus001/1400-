arr = [3, 5, 2, 8, 5, 9, 1]
max_val = max(arr)
min_val = min(arr)
max_index = arr.index(max_val)
min_index = arr.index(min_val)
print("Max before min" if max_index < min_index else "Min before max")
