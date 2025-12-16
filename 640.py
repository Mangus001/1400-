n = int(input())
a = [int(input()) for _ in range(n)]
max_a = max(a)
min_a = min(a)
print(max_a - min_a <= 25)
