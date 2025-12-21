k = int(input())
word = input()
new_word = word[k:] + word[:k]
print(new_word)
word = input()
k = int(input())
res = ""
for i in range(k, len(word)):
    res += word[i]
for i in range(0, k):
    res += word[i]
print(res)
