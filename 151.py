t = float(input())

cycle_position = t % 5

if cycle_position < 3:
    print("Зеленый сигнал")
else:
    print("Красный сигнал")
