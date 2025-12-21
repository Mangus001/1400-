import math

for i in range(len(arr)):
    if arr[i] > 10:
        arr[i] = math.sqrt(arr[i])

for i in range(0, len(arr), 2):
    arr[i] = abs(arr[i])
