arr = [1, 2, 3, 4, 5]
k = 3
arr = arr[:-1] + [arr[-1]] + arr[k-1:-1]
