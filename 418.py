distance = 10
day = 1
total = 10

while distance <= 20:
    day += 1
    distance *= 1.1  
print("День, когда пробежит больше 20 км:", day)


distance = 10
total = 10
day = 1
while total <= 100:
    day += 1
    distance *= 1.1
    total += distance
print("Количество дней, когда суммарный пробег превысит 100 км:", day)
