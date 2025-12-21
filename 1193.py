s = input()
chars = list(s)
for i in range(1, len(chars)+1):
    if i % 2 == 0:
        chars[i-1] = 'ы'
print(''.join(chars))
