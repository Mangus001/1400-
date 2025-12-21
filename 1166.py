sentence = input()
first_e = sentence.find('е')
last_e = sentence.rfind('е')
print(first_e + 1, last_e + 1)
