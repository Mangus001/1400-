def last_occurrence_position(sentence, letter):
    return sentence.rfind(letter)  

sentence1 = "Это пример предложения с й по последнему вхождению й"
sentence2 = "Нет буквы й здесь"

pos1 = last_occurrence_position(sentence1, 'й')
pos2 = last_occurrence_position(sentence2, 'й')

if pos1 > pos2:
    print("В первом предложении буква 'й' имеет больший порядковый номер")
else:
    print("Во втором предложении буква 'й' имеет больший порядковый номер или отсутствует")
