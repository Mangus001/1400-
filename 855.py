def task_1137_a(arr, a1, b):
    return [x + arr[a1] if x < 0 else x for x in arr], [x - b if x == 0 else x for x in arr]

def task_1137_b(arr, a, b, c):
    return [x - a if x > 0 else x for x in arr], [x - b if x < 0 else x for x in arr], [x + c if x == 0 else x for x in arr]
