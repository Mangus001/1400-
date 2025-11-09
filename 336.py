import math

length = 4.5 
x = 3.0 
max_x = math.sqrt(length**2 - 0**2)  

while x <= length:
    if x > length:
        break
    cos_theta = x / length
    theta_rad = math.acos(cos_theta)
    theta_deg = math.degrees(theta_rad)
    print(f"Расстояние: {x:.2f} м, угол: {theta_deg:.2f} градусов")
    x += 0.2
