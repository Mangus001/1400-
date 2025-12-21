word = "abcdefghij12"  
a = word[:4]
b = word[4:8]
c = word[8:]
part1 = c
part2 = a
part3 = b
new_word_a = part1 + part2 + part3
print(new_word_a)
part1_b = b
part2_b = c
part3_b = a
new_word_b = part1_b + part2_b + part3_b
print(new_word_b)
