sentence = input()
words = sentence.split()
from collections import Counter
counter = Counter(words)
duplicates = [w for w in set(words) if counter[w]==2]
print(' '.join(duplicates))
