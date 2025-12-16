score_player = 0
score_computer = 0
import sys

user_guess = int(input("Чет (введите 2) или нечет (введите 1): "))
computer_choice = random.randint(1, 2)
if user_guess == computer_choice:
    print("Вы выиграли!")
else:
    print("Вы проиграли!")

n = int(input("Введите количество раундов: "))
score_player = 0
score_computer = 0
for _ in range(n):
    user_guess = int(input("Чет (2) или нечет (1): "))
    computer_choice = random.randint(1, 2)
    if user_guess == computer_choice:
        score_player += 1
    else:
        score_computer += 1
print(f"Счет {score_player}:{score_computer} в вашу пользу." if score_player > score_computer else f"Счет {score_player}:{score_computer} в пользу компьютера. Вы проиграли!")

score_player = 0
score_computer = 0
while True:
    user_guess = int(input("Чет (2) или нечет (1): "))
    computer_choice = random.randint(1, 2)
    if user_guess == computer_choice:
        score_player += 1
    else:
        score_computer += 1
    cont = input("Продолжить еще раз? (Да/Нет): ").lower()
    if cont == 'нет':
        break
print(f"Всего правильных: {score_player}, неправильно: {score_computer}")
