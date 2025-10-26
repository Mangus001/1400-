k = int(input())

d = 1
day_of_week = (d + k - 2) % 7 + 1

if day_of_week == 6:
    print("Суббота")
elif day_of_week == 7:
    print("Воскресенье")
else:
    print("Рабочий 

          
k = int(input())

# а) 1 января – понедельник (d=1)
d = 1
day_of_week = (d + k - 2) % 7 + 1

if day_of_week == 6:
    print("Суббота")
elif day_of_week == 7:
    print("Воскресенье")
else:
    print("Рабочий день")
