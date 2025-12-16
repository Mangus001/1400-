n = int(input())
d = [int(input()) for _ in range(n)]
max_length = 0
current_length = 0
for i in range(n):
    if d[i] % 2 == 0:
        current_length += 1
        if current_length > max_length:
            max_length = current_length
    else:
        current_length = 0
print(max_length)
