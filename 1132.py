word1 = input()
word2 = input()
len_diff = len(word2)
modified = word1[:len_diff] + word2[len_diff:]
print(modified)
