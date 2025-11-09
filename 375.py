password = 12345 
while True:
    attempt = int(input("Введите пароль: "))
    if attempt == password:
        print("Доступ разрешен. Приветствие.")
        break
    else:
        print("Ошибка, повторите.")
