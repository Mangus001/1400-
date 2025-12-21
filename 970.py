arr = [1, 2, 3, 4, 5]
arr[1], arr[4] = arr[4], arr[1]
m, n = 2, 4
arr[m-1], arr[n-1] = arr[n-1], arr[m-1]
max_value = max(arr)
max_idx = arr.index(max_value)
arr[2], arr[max_idx] = arr[max_idx], arr[2]
min_value = min(arr)
min_idx = len(arr) - 1 - arr[::-1].index(min_value)
arr[0], arr[min_idx] = arr[min_idx], arr[0]
print(arr)
