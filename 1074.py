arr = [int(input()) for _ in range(20)]
b = [x for x in arr if x < 0] + [x for x in arr if x >= 0]
