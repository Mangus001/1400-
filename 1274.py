word1 = input()
word2 = input()
set1 = set(word1)
set2 = set(word2)
common = set1 & set2
res = (set1 - common) | (set2 - common)
print(''.join(res))
