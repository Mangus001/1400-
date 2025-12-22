word = input()
from collections import Counter
cnt = Counter(word.lower())
for letter, count in cnt.items():
    if count == 2:
        print(letter)
        break
