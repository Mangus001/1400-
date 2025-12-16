scores = list(map(int, input().split()))
is_sorted = all(scores[i] >= scores[i+1] for i in range(len(scores)-1))
print(is_sorted)
