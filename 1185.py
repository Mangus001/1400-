words = input().split()
correct = True
for w in words:
    if 'жи' in w:
        correct = False
    if 'ши' in w:
        correct = False
print('правильно' if correct else 'неправильно')
