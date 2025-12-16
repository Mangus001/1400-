n = int(input())
p = float(input())
b = [float(input()) for _ in range(n)]
total = sum(x for x in b if x > p)
print(total)
