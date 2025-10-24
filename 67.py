n = int(input("Введите количество секунд с начала суток: "))

hours = n // 3600
remaining_seconds_after_hours = n % 3600
minutes = remaining_seconds_after_hours // 60
seconds = remaining_seconds_after_hours % 60

print(f"Полных часов: {hours}")
print(f"Полных минут с начала текущего часа: {minutes}")
print(f"Полных секунд с начала текущей минуты: {seconds}")
