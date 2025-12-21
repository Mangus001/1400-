def task1182(arr):
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] % 10 == 0 and arr[i + 1] % 10 == 0:
            count += 1
    return count
