a, b = map(int, input().split())

max_div_count = -1
min_div_count = float('inf')
max_num = None
min_num = None

for num in range(a, b+1):
    c = divisor_count(num)
    if c > max_div_count:
        max_div_count = c
        max_num = num
    if c < min_div_count:
        min_div_count = c
        min_num = num

print("Максимальное число с максимумом делителей:", max_num)
print("Минимальное число с максимумом делителей:", min_num)
