import statistics
n = int(input())
scores = [float(input()) for _ in range(n)]
max_score = max(scores)
min_score = min(scores)

scores.remove(max_score)
scores.remove(min_score)

average = sum(scores) / len(scores)
print(average)
