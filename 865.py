def task_1147(arr):
    inv = sum(1/x for x in arr if x != 0)
    return len(arr) / inv if inv != 0 else float('inf')
