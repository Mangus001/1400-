def count_letter_in_sentence(sentence, letter):
    return sentence.lower().count(letter.lower())

def total_letter_in_sentences(sentences, letter):
    total = 0
    for s in sentences:
        total += count_letter_in_sentence(s, letter)
    return total

sentences = [
    "Первая фраза",
    "Вторая фраза",
    "Третья фраза"
]
print(total_letter_in_sentences(sentences, 'е'))
