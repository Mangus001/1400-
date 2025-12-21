d = [float(input()) for _ in range(15)]
w = [float(input()) for _ in range(15)]
h = [float(input()) for _ in range(15)]

max_vol = d[0]*w[0]*h[0]
min_vol = d[0]*w[0]*h[0]
max_idx = 0
min_idx = 0
for i in range(1, 15):
    vol = d[i]*w[i]*h[i]
    if vol > max_vol:
        max_vol = vol
        max_idx = i
    if vol < min_vol:
        min_vol = vol
        min_idx = i
print("Максимальный объем", max_vol)
print("Минимальный объем", min_vol)
print("Индекс фигуры с максимальным объемом", max_idx)
print("Индекс фигуры с минимальным объемом", min_idx)

volumes = [d[i]*w[i]*h[i] for i in range(15)]
print("Максимальный объем", max(volumes))
print("Минимальный объем", min(volumes))
print("Индекс с максимальным объемом", volumes.index(max(volumes)))
print("Индекс с минимальным объемом", volumes.index(min(volumes))
