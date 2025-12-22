sentence = input()
words = sentence.split()
lengths = [len(w) for w in words]
print(min(lengths) if lengths else 0)
