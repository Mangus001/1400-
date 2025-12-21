word = input()
if len(word) >= 6:
    transformed = word[3:-3] + word[:3] + word[-3:]
    print(transformed)
