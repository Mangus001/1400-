sentence = input()
words = sentence.split()
for w in words:
    if w != 'привет':
        print(w)
