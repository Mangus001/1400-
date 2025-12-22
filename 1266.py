word = input()
letters = set()
for ch in word:
    if ch.isalpha():
        letters.add(ch.lower())
print(len(letters))
