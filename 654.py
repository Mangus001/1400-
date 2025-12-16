k = int(input())
precipitations = list(map(int, input().split()))
max_precip = precipitations[0]
day = 1
for i in range(1, k):
    if precipitations[i] >= max_precip:
        max_precip = precipitations[i]
        day = i + 1
print(day)
