s = input('Введите предложение: ')
char1 = input('Введите первый символ: ')
char2 = input('Введите второй символ: ')
for ch in s:
    if ch == char1 or ch == char2:
        print(ch)
