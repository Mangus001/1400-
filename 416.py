digits = [int(d) for d in str(n)]
max_digit = max(digits)
min_digit = min(digits)
pos_max = pos_min = 0
for i, d in enumerate(digits):
    if d == max_digit:
        pos_max = i
        break
for i, d in enumerate(digits):
    if d == min_digit:
        pos_min = i
        break
print("Максимальная левая:", "да" if pos_max < pos_min else "нет")
print("Минимальная левая:", "да" if pos_min < pos_max else "нет")
