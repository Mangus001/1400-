game_results = list(map(int, input().split()))
game_results_str = input()
length = len(game_results_str)
scores = []
for ch in game_results_str:
    scores.append(int(ch))
results = []
won = 0
lost = 0
drawn = 0
for g in scores:
    if g // 10 > g % 10:
        results.append('выигрыш')
        won +=1
    elif g // 10 < g % 10:
        results.append('проигрыш')
        lost +=1
    else:
        results.append('ничья')
        drawn +=1
print('Выигрышей:', won)
print('Проигрышей:', lost)
print('Ничьих:', drawn)
