sentence = input()
import re
first_sentence = sentence
words = first_sentence.split()
print(len([ch for ch in first_sentence if ch in 'ий']))
