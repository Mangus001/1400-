m = int(input())
scores = list(map(int, input().split()))
min_score = scores[0]
min_index = 0
for i in range(1, m):
    if scores[i] < min_score:
        min_score = scores[i]
        min_index = i
print(min_index + 1)
