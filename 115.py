import math

inner_radius = 5  
thickness = 0.5  
num_shards = 12

total_volume = 0
for i in range(num_shards):
    radius = inner_radius + i * thickness
    volume = (4/3) * math.pi * radius ** 3
    total_volume += volume

total_volume_liters = total_volume * 0.001
print(f"Общий объем вложенных шаров: {total_volume_liters:.2f} литров")
