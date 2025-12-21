def task1177(arr):
    positives = sum(1 for x in arr if x > 0)
    negatives = sum(1 for x in arr if x < 0)
    return positives, negatives
