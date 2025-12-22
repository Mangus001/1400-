word = input()
idx = word.find('о')
if idx != -1:
    word = word[:idx] + word[idx+1:]
print(word)
