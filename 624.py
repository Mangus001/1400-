sequence = []
while True:
    num = float(input())
    sequence.append(num)
    if num == 1000:
        break
count_equal = 1
for i in range(1, len(sequence)):
    if sequence[i] == sequence[i-1]:
        count_equal += 1
print(count_equal)
