sequence = list(map(int, input().split()))
max_count = 1
current_count = 1
for i in range(1, len(sequence)):
    if sequence[i] == sequence[i-1]:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 1
print(max_count)
