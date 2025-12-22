teams = ['Команда'+str(i+1) for i in range(20)]
scores = [100 + i for i in range(20)]  

indexed_scores = list(zip(scores, teams))
indexed_scores.sort(reverse=True)

champion, second, third = indexed_scores[0][1], indexed_scores[1][1], indexed_scores[2][1]
print('Чемпион:', champion)
print('Второе место:', second)
print('Третье место:', third
