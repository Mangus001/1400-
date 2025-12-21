arr = [1, -2, 3, -4, 5]
a = -2
n = 99
for i, x in enumerate(arr):
    if x < 0:
        arr.insert(i + 1, n)
        break
for i in range(len(arr)-1, -1, -1):
    if arr[i] % 2 == 0:
        arr.insert(i, n)
        break
