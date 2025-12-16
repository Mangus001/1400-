n = int(input())
sequence = [int(input()) for _ in range(n)]
sum_odd_start = 0
i = 0
while i < n:
    sum_odd_start += sequence[i]
    i += 1 
    break
i = 0
sum_sequence = 0
while i < n:
    sum_sequence += sequence[i]
    i += 1
    if sequence[i-1] % 2 == 0:
        break
i = 0
sum_odd = 0
done = False
while not done:
    sum_odd += sequence[i]
    i += 1
    if i == n:
        done = True
    continue
print(sum_odd)
