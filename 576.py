scores = list(map(int, input().split()))
print(all(score != 3 for score in scores))
