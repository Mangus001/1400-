equence = list(map(int, input().split()))
A_zero = sequence.count(8)
sequence.append(int(input()))
A_eight_sequence = sequence.copy()
A_eight_sequence[-1] = 8
A_eight = A_eight_sequence.count(8)
print(A_zero)
print(A_eight)
