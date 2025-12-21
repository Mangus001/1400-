def task1196(arr):
    min_val = min(arr)
    max_val = max(arr)
    avg_min_max = (min_val + max_val) / 2
    return [i+1 for i, x in enumerate(arr) if x > avg_min_max]
