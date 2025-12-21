def task_1135_a(arr, m1, m2):
    return [x + arr[m1] if x < 0 else x + arr[m2] for x in arr]

def task_1135_b(arr):
    return [x * 2 if i % 2 == 0 else x - 1 for i, x in enumerate(arr)]
