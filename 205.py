t = float(input())
t %= 60
cycle_time = t % 9

if cycle_time < 3:
    print("Зеленый")
elif cycle_time < 4:
    print("Желтый")
elif cycle_time < 6:
    print("Красный")
else:
    print("Зеленый")
