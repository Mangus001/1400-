expression = input()
total = 0
sign = 1
for ch in expression:
    if ch == '+':
        sign = 1
    elif ch == '-':
        sign = -1
    elif ch.isdigit():
        total += sign * int(ch)
print(total)
