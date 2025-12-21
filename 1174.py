s = input()
words = s.split()
print(max(words, key=len))
