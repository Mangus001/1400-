s = input()
k = int(input())
s = s[:-1]
s = s[:k] + 'т' + s[k:]
print(s)
