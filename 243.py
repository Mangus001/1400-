x, y = map(float, input("Введите координаты x и y: ").split())

if x > 0 and y > 0:
    print("1-я четверть")
elif x < 0 and y > 0:
    print("2-я четверть")
elif x < 0 and y < 0:
    print("3-я четверть")
elif x > 0 and y < 0:
    print("4-я четверть")
