m = float(input())
for x in range(1, 101):
    y = math.log(x)
    if y < m:
        print(y)
