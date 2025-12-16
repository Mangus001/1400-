scores_t1 = list(map(int, input().split()))
scores_t2 = list(map(int, input().split()))
print("Первый лучше" if sum(scores_t1) > sum(scores_t2) else "Второй лучше" if sum(scores_t1) < sum(scores_t2) else "Равны")
