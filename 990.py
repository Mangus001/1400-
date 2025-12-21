arr = [1, 2, 3]
max_elem = max(arr)
for i, x in enumerate(arr):
    if x == max_elem:
        arr.insert(i + 1, 99)
        arr.insert(i + 1, 88)
        break
