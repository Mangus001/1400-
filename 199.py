y_birth = int(input("Год рождения: "))
m_birth = int(input("Месяц рождения: "))
d_birth = int(input("День рождения: "))

y_today = int(input("Текущий год: "))
m_today = int(input("Текущий месяц: "))
d_today = int(input("Текущий день: "))

age = y_today - y_birth

if m_today < m_birth or (m_today == m_birth and d_today < d_birth):
    age -= 1

print(f"Возраст: {age} полных лет")
