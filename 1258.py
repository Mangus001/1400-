import re
text = input()
matches = re.findall(r'\d+', text)
max_number = ''
for match in matches:
    if len(match) > len(max_number):
        max_number = match
print(max_number
