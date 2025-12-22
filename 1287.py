sentence = input()
from collections import Counter
words = sentence.split()
counter = Counter(words)
for w in words:
    if counter[w]==1:
        print(w, end=' ')
print()
