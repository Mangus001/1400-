s = input('Введите предложение: ')
index = s.find('нн')
while index != -1:
    print('нн на позиции:', index)
    index = s.find('нн', index + 1)
