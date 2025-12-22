word1 = input()
word2 = input()
for ch in word1:
    if ch.isalpha():
        print('да' if ch in word2 else 'нет', end=' ')
