m = int(input())
sequence = [int(input()) for _ in range(m)]
max_len = 0
current_len = 0
for num in sequence:
    if num == 0:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    else:
        current_len = 0
print(max_len)
