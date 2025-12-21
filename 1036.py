scores = list(map(int, input().split()))
total = len(scores)
fives_count = len([score for score in scores if score == 5])
print(fives_count)
