word1 = input()
word2 = input()
from collections import Counter
cnt1 = Counter(word1)
cnt2 = Counter(word2)
res = []
for ch in set(word1):
    if cnt1[ch]==1 and cnt2.get(ch,0)==1:
        res.append(ch)
print(' '.join(res))
