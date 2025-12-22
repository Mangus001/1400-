s = input()
result = ''
for ch in s:
    if ch == 'a':
        result += 'б'
    elif ch == 'б':
        result += 'а'
    elif ch == 'А':
        result += 'Б'
    elif ch == 'Б':
        result += 'А'
    else:
        result += ch
print(result)
