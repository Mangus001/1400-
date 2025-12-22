s = input()
k = int(input())
s = list(s)
s = s[k-1:] + s[:k-1]
s = ''.join(s)
print(s)
