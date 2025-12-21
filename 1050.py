z = list(map(int, input().split()))
o = list(map(int, input().split()))
results = []
points = {'выигрыш':3, 'ничья':1, 'проигрыш':0}
win_count = 0
lose_count = 0
draw_count = 0
for zg, oz in zip(z, o):
    if zg > oz:
        results.append('выигрыш')
        win_count +=1
    elif zg < oz:
        results.append('проигрыш')
        lose_count +=1
    else:
        results.append('ничья')
        draw_count +=1
print(*results)
print('Всего побед:', win_count)
print('Всего поражений:', lose_count)
