sequence = []
while True:
    num = int(input())
    sequence.append(num)
    if num == 100:
        break
first_666 = 0
for i, val in enumerate(sequence):
    if val == 666:
        first_666 = i + 1
        break
print(first_666)
