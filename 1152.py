sentence = input()
vowels = 'аеёиоуыэюя'
count_vowels = sum(ch in vowels for ch in sentence)
print(count_vowels)
