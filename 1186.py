words = input().split()
correct = True
for w in words:
    if 'ча' in w:
        correct = False
        w = w.replace('ча', 'ща')
    if 'ща' in w:
        correct = False
print('правильно' if correct else 'неправильно')
