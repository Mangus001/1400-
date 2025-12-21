def task_1163(arr):
    total = 0
    for i, month in enumerate(arr, start=1):
        if month in [3, 6, 9, 12]:
            total += month
    return total
