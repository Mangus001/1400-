sentence = input()
count_o = sentence.count('о')
count_a = sentence.count('а')
print('о' if count_o > count_a else 'а')
