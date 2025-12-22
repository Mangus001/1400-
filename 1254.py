expression = input()
parts = expression.split('+')
total = 0
for part in parts:
    d = part.strip()
    if d.isdigit():
        total += int(d)
print(total m
