def task_1134(arr, k1, k2):
    return [x - arr[k1] if x > 0 else x - arr[k2] for x in arr]

def task_1134_b(arr):
    return [x + 1 if i % 2 != 0 else x - 1 for i, x in enumerate(arr)]
