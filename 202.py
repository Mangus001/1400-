a = int(input())
b = int(input())
c = int(input())
d = int(input())
n = int(input())
m = int(input())

arrival_time = a * 60 + b
departure_time = c * 60 + d
visit_time = n * 60 + m

if arrival_time <= visit_time <= departure_time:
    print("Да")
else:
    print("Нет")
