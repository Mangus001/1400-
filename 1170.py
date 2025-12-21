sequence = input()
import itertools
first_char = sequence[0]
count = 1
for ch in sequence[1:]:
    if ch == first_char:
        count += 1
    else:
        break
print(count)
