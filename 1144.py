s = input('Введите предложение: ')
total_letters = sum(c.isalpha() for c in s)
a_count = s.count('а')
percentage = (a_count / total_letters) * 100 if total_letters > 0 else 0
print(f'Доля букв "а": {percentage:.2f}%')
