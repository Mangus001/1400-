s = input()
pos = s.find('а')
print('есть' if pos != -1 else 'нет')
if pos != -1:
    print(pos+1)
