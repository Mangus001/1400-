def task1195(arr):
    total_sum = sum(arr)
    return [i+1 for i, x in enumerate(arr) if x > total_sum]
