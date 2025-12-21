def task1165(arr):
    a = sum(x for x in arr if x > 20) > 100
    b = sum(x for x in arr if x < 50) % 2 == 0
    return a, b
