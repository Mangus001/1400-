rain_data = [(10, 5), (0, 10), (15, 0)] 
snow = sum(r for r, t in rain_data if t <= 0)
rain_only = sum(r for r, t in rain_data if t > 0)
