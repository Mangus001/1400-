def task1181(arr):
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] % 2 == 0 and arr[i + 1] % 2 == 0:
            count += 1
    return count
