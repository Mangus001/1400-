seq = input()
first_char = seq[0]
count = 0
for ch in seq:
    if ch == first_char:
        count +=1
    else:
        break
print(count)
