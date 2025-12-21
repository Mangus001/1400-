arr = [1, -2, 3, -4, 5]
n = 99
result = []
i = 0
while i < len(arr) - 1:
    result.append(arr[i])
    if arr[i] * arr[i + 1] > 0:
        result.append(n)
    i += 1
result.append(arr[-1])
max_size = len(result)
