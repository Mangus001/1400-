sentence = input()
words = sentence.split()
max_word = max(words, key=len) if words else ''
print(max_word)
