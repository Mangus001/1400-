arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
arr = [x for i, x in enumerate(arr, 1) if not (i % 2 == 1 and x % 2 == 0)]
arr = [x for x in arr if not (x % 3 == 0 or x % 5 == 0)]
