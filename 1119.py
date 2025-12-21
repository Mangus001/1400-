word = "словаслова"
length = len(word)
half = length // 2
first_half = word[:half]
second_half = word[half:]
result = second_half + first_half
print(result)
