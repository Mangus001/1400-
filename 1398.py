def is_palindrome_word(word):
    return word.lower() == word.lower()[::-1]

words = ["Кирик", "Катак"]
for w in words:
    print(f"{w} — палиндром: {is_palindrome_word(w)}")
