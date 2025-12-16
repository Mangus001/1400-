n = int(input())
a = [int(input()) for _ in range(n)]
print(a[0] + a[-1])
if n >= 2:
    print(a[1] - a[-2])
