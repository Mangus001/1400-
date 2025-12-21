def task_1142(arr, k1, k2, s1, s2):
    sum_all = sum(arr)
    prod_all = 1
    sum_squares = 0
    sum_first_six = sum(arr[:6])
    sum_k1_k2 = sum(arr[k1:k2+1])
    sum_all /= len(arr)
    sum_range = sum(arr[s1-1:s2])
    for x in arr:
        prod_all *= x
        sum_squares += x ** 2
    return sum_all, prod_all, sum_squares, sum_first_six, sum_k1_k2, sum_all, sum_range / (s2 - s1 + 1)
