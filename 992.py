arr = [1, 3, 5, 7, 9]
n = 4
m = 6
result = [n]
for x in arr:
    if x > n:
        result.append(x)
result2 = []
for x in arr:
    result2.append(x)
    if x < m:
        result2.append(m)
