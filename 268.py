import math

R = 6350 
for h in range(1, 11):
    D = math.sqrt(2 * R * h)
    print(f"Высота: {h} км, Расстояние до горизонта: {D:.2f} км")
