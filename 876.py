def task_1158(arr):
    min_obl = max_obl = arr[0]
    for i, score in enumerate(arr):
        if i < 6:
            min_obl = min(min_obl, score)
            max_obl = max(max_obl, score)
        else:
            min_vol = min(min_obl, score)
            max_vol = max(max_obl, score)
    return max(max_obl, max_vol)
