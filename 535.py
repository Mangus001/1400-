n = int(input())
temps = [float(input()) for _ in range(n)]
count_below_zero = 0
i = 0
while i < n:
    count_below_zero += (temps[i] < 0)
    i += 1
