s = input()
first_comma = s.find(',')
second_comma = s.find(',', first_comma + 1)
if second_comma != -1:
    print(s[first_comma+1:second_comma])
elif first_comma != -1:
    print(s[first_comma+1:])
else:
    print('Нет запятых')
