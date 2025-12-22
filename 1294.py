sent1 = input().split()
sent2 = input().split()
for w in sent1:
    if w not in sent2:
        print(w)
for w in sent2:
    if w not in sent1:
        print(w)
