arr = [1, 2, 2, 3, 4, 3, 5]
seen = set()
result = []
for x in arr:
    if x not in seen:
        seen.add(x)
        result.append(x)
arr = result
