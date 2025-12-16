a = float(input())
denom = 1
while True:
    num = 1 / denom
    if num < a:
        print(num)
        break
    denom += 1
