text = input()
import re
match = re.search(r'(.)\1\1\1\1', text)
print('Есть' if match else 'Нет')
