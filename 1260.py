import re
text = input()
numbers = re.findall(r'\d+', text)
max_number = max([int(num) for num in numbers]) if numbers else None
print(max_number)
