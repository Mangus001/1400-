sequence = list(map(int, input().split()))
max_length_inc = 1
max_length_dec = 1
current_inc = 1
current_dec = 1
for i in range(1, len(sequence)):
    if sequence[i] > sequence[i-1]:
        current_inc += 1
    else:
        current_inc = 1
    if sequence[i] < sequence[i-1]:
        current_dec += 1
    else:
        current_dec = 1
    if current_inc > max_length_inc:
        max_length_inc = current_inc
    if current_dec > max_length_dec:
        max_length_dec = current_dec
print(max_length_inc, max_length_dec)
