sentence = input()
words = sentence.split()
longest = max(words, key=len) if words else ''
print(len(longest)>10)
