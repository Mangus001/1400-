a = float(input())
denom = 1
while True:
    num = 1 / denom
    if num < a:
        break
    print(num)
    denom += 1
