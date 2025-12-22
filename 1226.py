s = input()
k = int(input())
letter = input()
s = s[:-1]
s = s[:k] + letter + s[k:]
print(
