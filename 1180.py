w1 = input()
w2 = input()
max_common = min(len(w1), len(w2))
match_count = 0
for i in range(max_common):
    if w1[i] == w2[i]:
        match_count += 1
    else:
        break
print(match_count)
