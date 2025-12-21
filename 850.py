import math
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = abs(arr[i])

for i in range(1, len(arr), 2):
    arr[i] = math.sqrt(arr[i])
