sentence = input()
words = sentence.split()
for w in words:
    if len(w)>0 and w[0]==w[-1]:
        print(w, end=' ')
print()
for w in words:
    if w.count('е')==3:
        print(w, end=' ')
print()
for w in words:
    if 'о' in w:
        print(w, end=' ')
print()
