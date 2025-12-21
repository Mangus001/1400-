def task1164(arr):
    pos_sum = sum(x for x in arr if x > 0)
    neg_sum = sum(x for x in arr if x < 0)
    return pos_sum / abs(neg_sum) if neg_sum != 0 else None
