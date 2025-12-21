def task_1139_a(arr):
    return [0 if x % 10 == 0 else x for x in arr]

def task_1139_b(arr, m):
    return [x * 2 if x % 2 != 0 else x // 2 for x in arr]

def task_1139_c(arr, m, n):
    return [x - m if x % 2 != 0 else x for x in arr], [x + n if i % 2 != 0 else x for i, x in enumerate(arr)]
