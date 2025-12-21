arr = [1, -2, 3, -4, 6]
n = 4
arr = [x for x in arr if x >= 0]
n_value = 4
arr = [x for x in arr if x <= n_value]
n1, n2 = 2, 4
arr = arr[:n1-1] + arr[n2:]
