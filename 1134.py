symbol = input("Введите символ: ")
sentence = input("Введите предложение: ")
for i, ch in enumerate(sentence):
    if ch == symbol:
        print(i)
