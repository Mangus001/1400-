arr = [1, -2, 3, -4, 5]
for i, val in enumerate(arr):
    if val < 0:
        del arr[i]
        break
for i in range(len(arr)-1, -1, -1):
    if arr[i] % 2 == 0:
        del arr[i]
        brea
