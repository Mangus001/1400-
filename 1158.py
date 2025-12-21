sentence = input()
comma_index = sentence.find(',')
if comma_index != -1:
    print(sentence[:comma_index])
else:
    print(sentence)
