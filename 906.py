def task1188(arr, m):
    smaller_than_m = [x for x in arr if x < m]
    return sum(smaller_than_m) / len(smaller_than_m) if smaller_than_m else None
