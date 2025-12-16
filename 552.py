n = int(input())
sequence = [float(input()) for _ in range(n)]
count_before_zero = 0
i = 0
while i < n:
    if sequence[i] == 0:
        break
    count_before_zero += 1
    i += 1
