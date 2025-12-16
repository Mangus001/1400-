correct_answers = 0
for _ in range(20):
    a = random.randint(1,9)
    b = random.randint(1,9)
    answer = int(input(f"Чему равно произведение {a}×{b}? "))
    if answer == a*b:
        correct_answers += 1
print(f"Правильных ответов: {correct_answers}")
while True:
    a = random.randint(1,9)
    b = random.randint(1,9)
    answer = int(input(f"Чему равно произведение {a}×{b}? "))
    if answer == 0:
        break
    if answer == a*b:
        print("Правильно")
    else:
        print("Неправильно")
