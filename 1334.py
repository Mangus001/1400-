athletes = ['Спортсмен'+str(i+1) for i in range(20)]
import random
scores = [[random.randint(0, 100) for _ in range(5)] for _ in range(20)]
total_scores = [sum(s) for s in scores]
max_idx = total_scores.index(max(total_scores))
print('Победитель –', athletes[max_idx])
