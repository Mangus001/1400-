a = float(input())
n = 1
while True:
    value = 1 + 1 / n
    if value < a:
        print(value)
    else:
        break
    n += 1
