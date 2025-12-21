arr = [3, -7, 2, -9, 4]
abs_max_value = max(arr, key=abs)
max_idx = arr.index(abs_max_value)
arr[max_idx] = -arr[max_idx]
print(arr)
