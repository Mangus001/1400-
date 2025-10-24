X = float(input("Введите возраст Тани: "))
Y = float(input("Введите возраст Мити: "))

average_age = (X + Y) / 2

diff_Tanya = abs(X - average_age)
diff_Mitya = abs(Y - average_age)

print(f"Средний возраст: {average_age:.2f} лет")
print(f"Разница возраста Тани от среднего: {diff_Tanya:.2f} лет")
print(f"Разница возраста Мити от среднего: {diff_Mitya:.2f} лет")
