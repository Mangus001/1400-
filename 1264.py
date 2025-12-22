text = input()
max_spaces = 0
current_spaces = 0
for ch in text:
    if ch == ' ':
        current_spaces +=1
        max_spaces = max(max_spaces, current_spaces)
    else:
        current_spaces=0
print(max_spaces)
