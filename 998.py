arr = [1, 2, 3, 4, 5]
s, k = 2, 4
arr = arr[:s-1] + arr[s:k] + [arr[s-1]] + arr[k:]
