word1 = input()
word2 = input()
from collections import Counter
cnt1 = Counter(word1)
cnt2 = Counter(word2)
possible1 = all(cnt2[ch] <= cnt1[ch] for ch in cnt2)
possible2 = all(cnt2[ch] == 0 or cnt1[ch] >= cnt2[ch] for ch in cnt2)
print('YES' if possible1 else 'NO')
print('YES' if possible2 else 'NO')
