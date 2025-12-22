word1 = input()
word2 = input()
res = []
for ch in word1:
    if (ch not in word2) and (ch.lower() not in word2.lower()):
        res.append(ch)
for ch in word2:
    if (ch not in word1) and (ch.lower() not in word1.lower()):
        res.append(ch)
print(' '.join(res))
