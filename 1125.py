s1 = input()
s2 = ""
for ch in s1:
    if ord(ch) % 2 == 1:
        s2 += ch
print(s2)
