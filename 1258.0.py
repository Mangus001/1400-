import re
text = input()
numbers = re.findall(r'\d+', text)
total = sum(int(num) for num in numbers)
print(total)
