k = int(input())
m = [int(input()) for _ in range(28)]
m = m[k:] + m[:k]
