a = float(input())
n = 1
while True:
    value = 1 + 1 / n
    if value < a:
        break
    print(n)
    n += 1
