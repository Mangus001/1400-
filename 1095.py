word = input()
k = int(input())  
if 1 <= k <= len(word):
    print(word[k-1])
else:
    print("Некорректный индекс")
