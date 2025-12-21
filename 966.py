arr = [5, 3, 9, 2, 8]
for i in range(len(arr)-1):
    if arr[i+1] < arr[i]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr[-1])
