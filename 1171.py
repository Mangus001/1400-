word1 = input()
word2 = input()
common = 0
for c1, c2 in zip(word1, word2):
    if c1 == c2:
        common +=1
    else:
        break
print(common)
