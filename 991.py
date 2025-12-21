arr = [1, 2, -3, 4]
a_value = 2
n_value = 5
for i, x in enumerate(arr):
    if x % a_value == 0:
        arr.insert(i, 99)
for i in range(len(arr)-1, -1, -1):
    if arr[i] < 0:
        arr.insert(i + 1, 88)
