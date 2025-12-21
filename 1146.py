sentence = input()
count = 0
for i in range(len(sentence)-1):
    if sentence[i] == sentence[i+1]:
        count +=1
print(count)
