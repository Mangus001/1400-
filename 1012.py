import bisect
array = sorted([int(input()) for _ in range(int(input()))])
a = int(input())
pos = bisect.bisect_left(array, a)
lesser = array[:pos]
n = int(input())
left, right = 0, len(array)-1
while left <= right:
    mid = (left + right) // 2
    if array[mid] < n:
        left = mid + 1
    else:
        right = mid - 1
import numpy as np
array_np = np.array(array)
idx = np.argmin(np.abs(array_np - a))
print(idx+1, array[idx])
