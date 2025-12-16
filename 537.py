n = int(input())
b = [int(input()) for _ in range(n)]
cnt_greater_p = 0
cnt_ending_5 = 0
cnt_multiple_k = 0
p = int(input())
k = int(input())
i = 0
while i < n:
    cnt_greater_p += (b[i] > p)
    cnt_ending_5 += (b[i] % 10 == 5)
    cnt_multiple_k += (b[i] % k == 0)
    i += 1
