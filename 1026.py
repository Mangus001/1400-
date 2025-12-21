arr = [int(input()) for _ in range(int(input()))]
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        print(*arr[i+2:])
        break
