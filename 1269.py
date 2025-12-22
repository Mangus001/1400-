word1 = input()
word2 = input()
unique_letters = set(word1.lower())
for ch in unique_letters:
    print('да' if ch in word2 else 'нет', end=' ')
