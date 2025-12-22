expr = input()
balance = 0
correct = True
for i, ch in enumerate(expr):
    if ch == '(':
        balance +=1
    elif ch == ')':
        if balance == 0:
            print(f"Лишняя правя скобка на позиции {i+1}")
            correct = False
            break
        balance -=1
if correct:
    if balance > 0:
        print(f"Лишних открывающих скобок: {balance}")
    else:
        print("да")
else:
    print("нет")
