arr = list(range(1, 16))
k, s = 3, 9
subset = arr[k-1:s]
arr[:k-1], arr[k-1:s], arr[s:] = subset[::-1], arr[k-1:s], subset[::-1]
k, s = 4, 8
subset = arr[k-1:s]
arr[:k-1], arr[k-1:s], arr[s:] = subset[::-1], arr[k-1:s], subset[::-1]
min_idx = arr.index(min(arr))
max_idx = arr.index(max(arr))
if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx
arr[min_idx:max_idx+1] = arr[min_idx:max_idx+1][::-1]
print(arr)
