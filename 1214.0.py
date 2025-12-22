idx = word.rfind('л')
if idx != -1:
    word = word[:idx] + word[idx+1:]
print(word)
