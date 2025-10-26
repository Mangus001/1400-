x, y = float(input()), float(input())
if y > x and y > -x:
    area = "I"
elif y < x and y > -x:
    area = "II"
elif y < x and y < -x:
    area = "III"
else:
    area = "На границе"
print(area)
