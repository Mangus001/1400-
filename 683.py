a = float(input())
n = 1
while True:
    last_num = 1 + 1 / n
    if last_num < a:
        print(n)
        break
    n += 1
