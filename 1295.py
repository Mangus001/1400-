sent1 = input().split()
sent2 = input().split()
common = set(sent1) & set(sent2)
for w in common:
    if sent1.count(w) == 1 and sent2.count(w) == 1:
        print(w)
