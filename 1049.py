missions = list(map(int, input().split()))
missed = list(map(int, input().split()))
results = []
for g, p in zip(missions, missed):
    if g > p:
        results.append('выигрыш')
    elif g < p:
        results.append('проигрыш')
    else:
        results.append('ничья')
print(*results)
