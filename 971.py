arr = list(range(10))
half = len(arr)//2
arr[:half], arr[half:] = arr[:half], arr[:half]
for i in range(0, len(arr), 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
for i in range(len(arr)//2):
    arr[i], arr[-1 - i] = arr[-1 - i], arr[i]
print(arr)
