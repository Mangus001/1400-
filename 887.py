ef task1169(arr, a):
    last = arr[-1]
    count_diff = sum(1 for x in arr if x != last)
    count_multiply = sum(1 for x in arr if a != 0 and x % a == 0)
    return count_diff, count_multiply
