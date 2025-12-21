indices = [0, 1, 4, 5, 8, 9]  
s = input('Введите предложение: ')
for i in indices:
    if i < len(s):
        print(s[i])
