word1 = input()
word2 = input()
word3 = input()
from collections import Counter
cnt1 = Counter(word1)
cnt2 = Counter(word2)
cnt3 = Counter(word3)
res1 = [ch for ch in cnt1 if (cnt1[ch]==1 and ch not in cnt2 and ch not in cnt3)]
res2 = [ch for ch in cnt1 if (ch not in cnt2 and ch not in cnt3)]
print(''.join(res1))
print(''.join(res2))
