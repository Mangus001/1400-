def task_1143(arr):
    total = 0
    sign = 1
    for i, x in enumerate(arr):
        if i % 2 == 0:
            total += x
        else:
            total -= x
    return total
