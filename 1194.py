s = input()
chars = list(s)
for i in range(len(chars)):
    if (i+1) % 3 == 0:
        chars[i] = 'а'
print(''.join(chars))
