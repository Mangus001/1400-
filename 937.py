scores = [random.uniform(1, 10) for _ in range(8)]
scores_sorted = sorted(scores)
scores_unique = [score for score in scores_sorted if scores_sorted.count(score) == 1]
scores_sorted.remove(scores_sorted[0])
scores_sorted.remove(scores_sorted[-1])
result = sum(scores_sorted)/len(scores_sorted)
print(result)
