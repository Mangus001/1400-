def count_letter_n(sentence):
    return sentence.count('н')

sentence1 = "Это пример предложения"
sentence2 = "Еще одно предложение"

total_n = count_letter_n(sentence1) + count_letter_n(sentence2)
print(f"Общее количество букв 'н': {total_n}"
