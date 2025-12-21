arr = [random.randint(1, 10) for _ in range(20)]
max_len = 0
current_len = 0
for num in arr:
    if num % 2 == 1:
        current_len += 1
        max_len = max(max_len, current_len)
    else:
        current_len = 0
print(max_len)
