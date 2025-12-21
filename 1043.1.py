goals = list(map(int, input().split()))
misses = list(map(int, input().split()))
total_goals = sum(goals) + sum(misses)
print(total_goals)
