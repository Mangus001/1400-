h = int(input())
m = int(input())

total_minutes = h * 60 + m

minute_angle = (m % 60) * 6  

hour_angle = (h % 12) * 30 + m * 0.5

diff = abs(hour_angle - minute_angle)
if diff > 180:
    diff = 360 - diff


k = 0
t = (diff + 360 * k) / 5.5
while t < 0:
    k += 1
    t = (diff + 360 * k) / 5.5

t = math.ceil(t)

print(t)
