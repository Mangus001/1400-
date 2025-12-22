sentence = input()
words = sentence.split()
found = None
for w in words:
    if w.startswith('к'):
        found=w
        break
print(found if found else '')
