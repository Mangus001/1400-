sequence = list(map(int, input().split()))
max_length = 0
current_length = 0
for i in range(len(sequence)):
    if i == 0 or sequence[i] > sequence[i-1]:
        current_length += 1
        if current_length > max_length:
            max_length = current_length
    else:
        current_length = 1
print(max_length)
