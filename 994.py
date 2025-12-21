arr = [1, 52, 3, 55, 6]
a = 5
count = sum(1 for x in arr if '5' in str(x))
max_size = len(arr) + count
