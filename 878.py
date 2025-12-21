def task_1160(arr, factor):
    s1 = sum(x for x in arr if x % 2 != 0)
    s2 = sum(x for x in arr if x % factor == 0)
    s3 = sum(x for x in arr if x % a == 0 or x % b == 0)
    return s1, s2, s3
