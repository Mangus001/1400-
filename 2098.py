word1 = input()
word2 = input()
print(word1[0] == word2[-1]) if len(word1) > 0 and len(word2) > 0 else print("Недостаточно символов")
