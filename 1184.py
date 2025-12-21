s = input()
pos_chu = s.find('чу')
pos_shu = s.find('щу')
print('есть' if pos_chu != -1 or pos_shu != -1 else 'нет')
if pos_chu != -1:
    print(pos_chu+1)
elif pos_shu != -1:
    print(pos_shu+1)
