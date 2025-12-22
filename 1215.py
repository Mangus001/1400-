s = input()
length = len(s)
if length % 2 == 1:
    s = s[:length//2] + s[length//2+1:]
else:
    s = s[:length//2 -1] + s[length//2 +1:]
print(s)
