km_per_hour = float(input())
m_per_second = float(input())

km_in_meters_per_second = km_per_hour * (1000 / 3600)

if km_in_meters_per_second > m_per_second:
    print("Скорость в километрах в час больше")
else:
    print("Скорость в метрах в секунду больше")
