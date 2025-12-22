sequence = input().split()
first_word = sequence[0]
result = []

for w in sequence[1:]:
    if w != first_word:
        if len(set(w)) == len(w):
            if w == w[::-1]:
                result.append(w)
print(' '.join(result))
