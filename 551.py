n = int(input())
sequence = [float(input()) for _ in range(n)]
count_negatives = 0
i = 0
while i < n and sequence[i] < 0:
    count_negatives += 1
    i += 1
