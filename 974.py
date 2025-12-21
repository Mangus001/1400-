arr = [1, -2, 3, -4, 5]
first_neg_idx = next((i for i, x in enumerate(arr) if x < 0), None)
last_pos_idx = next((i for i in range(len(arr)-1, -1, -1) if arr[i] > 0), None)
if first_neg_idx is not None and last_pos_idx is not None:
    arr[first_neg_idx], arr[last_pos_idx] = arr[last_pos_idx], arr[first_neg_idx]
print(arr)
