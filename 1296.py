text = input()
stack = []
positions = []
correct = True
for i, ch in enumerate(text):
    if ch == '(':
        stack.append(i)
    elif ch == ')':
        if stack:
            stack.pop()
        else:
            print(f"Лишняя правяя скобка на позиции {i+1}")
            correct = False
            break
if correct:
    if stack:
        print(f"Открывающих скобок: {len(stack)}")
    else:
        print("да")
else:
    print("нет")
