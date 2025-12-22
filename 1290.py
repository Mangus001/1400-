sentence = input()
words = sentence.split()

def replace_first_a(word):
    if 'a' in word:
        return 'o' + word[1:] if word[0] != 'a' else 'o' + word[1:]
    return word

def delete_last_char_except(word):
    if len(word) == 0:
        return word
    last_char = word[-1]
    return word[:-1].replace(last_char, '') + last_char

def first_occurrences(word):
    seen = set()
    result = ''
    for ch in word:
        if ch not in seen:
            seen.add(ch)
            result += ch
    return result

max_len = max(len(w) for w in words)
longest_words = [w for w in words if len(w) == max_len]
longest_word = longest_words[0]
mid = len(longest_word)//2
if len(longest_word) % 2 == 0:
    new_word = longest_word[:mid-1] + longest_word[mid+1:]
else:
    new_word = longest_word[:mid] + longest_word[mid+1:]
words = [replace_first_a(w) for w in words]
words = [delete_last_char_except(w) for w in words]
words = [first_occurrences(w) for w in words]
for i, w in enumerate(words):
    if w == longest_word:
        words[i] = new_word
print(' '.join(words))
