sentence = input()
words = sentence.split()
if words:
    words[0], words[-1] = words[-1], words[0]
print(' '.join(words))
