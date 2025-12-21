sentence = input()
import re
words = re.findall(r'\b\w+\b', sentence)
print(len(words))
sentence2 = input()
words2 = re.findall(r'\b\w+\b', sentence2.strip())
print(len(words2))
