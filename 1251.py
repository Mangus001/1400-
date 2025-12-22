text = input()
index_first_char = 0
while index_first_char < len(text) and text[index_first_char] == ' ':
    index_first_char += 1
sub_text = text[index_first_char:]
digits = [int(ch) for ch in sub_text if ch.isdigit()]
if digits:
    max_digit = max(digits)
    for i, ch in enumerate(sub_text):
        if ch.isdigit() and int(ch) == max_digit:
            position = index_first_char + i + 1
            print(position)
            break
