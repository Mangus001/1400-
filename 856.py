def task_1138_a(arr):
    return [x / 2 if x % 10 == 4 else x for x in arr]

def task_1138_b(arr):
    return [x ** 2 if x % 2 == 0 else x * 2 for x in arr]

def task_1138_c(arr, a, b):
    return [x + a for x in arr], [x - b if i % 2 == 0 else x for i, x in enumerate(arr)]
