def task1190(arr):
    pos_sum = sum(x for x in arr if x > 0)
    neg_sum = sum(x for x in arr if x < 0)
    count_pos = sum(1 for x in arr if x > 0)
    count_neg = sum(1 for x in arr if x < 0)
    avg_pos = pos_sum / count_pos if count_pos else None
    avg_neg = neg_sum / count_neg if count_neg else None
    return avg_pos, avg_neg
