sent1 = set(input().split())
sent2 = set(input().split())
for w in input().split():
    if w in sent2:
        print(w)
