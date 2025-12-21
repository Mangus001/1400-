s = input()
pos = -1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        pos = i+1
        break
if pos != -1:
    print(pos)
else:
    print('Нет таких пар')
