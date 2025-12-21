arr = [int(input()) for _ in range(int(input()))]
last_pair_end = -1
for i in range(len(arr)-1):
    if arr[i] % 2 == 0 and arr[i+1] % 2 == 0:
        last_pair_end = i+1
if last_pair_end != -1:
    print(*arr[:last_pair_end])
