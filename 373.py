n = int(input())
i = 1
while i <= 100:
    if i * i > n:
        print(i)
        break
    i += 1
