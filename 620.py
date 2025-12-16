sequence = []
while True:
    num = int(input())
    sequence.append(num)
    if num == -1:
        break
first_multiple_of_seven = 0
for i, val in enumerate(sequence):
    if val % 7 == 0:
        first_multiple_of_seven = i + 1
        break
print(first_multiple_of_seven)
