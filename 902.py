def task1184(arr):
    count_pos = sum(1 for x in arr if x > 0)
    count_leq_50_55 = sum(1 for x in arr if x <= 50.55)
    a = count_pos <= 5
    b = count_leq_50_55 % 4 == 0
    return a, b
