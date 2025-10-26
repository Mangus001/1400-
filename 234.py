x, y = float(input()), float(input())
if y > 0 and y < x:
    area = "I"
elif y < 0 and y > -x:
    area = "II"
elif y > 0 and y > x:
    area = "III"
else:
    area = "На границе"
print(area)
