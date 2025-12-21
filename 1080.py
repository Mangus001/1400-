arr = [int(input()) for _ in range(10)]
res3 = []
for x in arr:
    if x != 13:
        res3.append(x)
res4 = [x for x in arr if x != 13]
