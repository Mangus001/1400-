groups_scores = []
for _ in range(3):
    scores = [list(map(float, input().split())) for _ in range(20)]
    avg = sum(sum(student) for student in scores) / (20 * 3)
    groups_scores.append(avg)

best_group = groups_scores.index(max(groups_scores)) + 1
print("Лучшая группа по среднему баллу:", best_group)
