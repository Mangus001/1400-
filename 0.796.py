user_guess = int(input("Чет (введите 2) или нечет (введите 1): "))
computer_choice = random.randint(1, 2)
if user_guess == computer_choice:
    print("Вы выиграли!")
else:
    print("Вы проиграли!")
