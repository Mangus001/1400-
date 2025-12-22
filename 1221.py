s = input()
s = ''.join([ch for i, ch in enumerate(s, start=1) if not (ch == 'о' and i % 2 == 1)])
print(s)
