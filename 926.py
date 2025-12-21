arr = [random.randint(-100, 100) for _ in range(20)]
sign_changes = 0
for i in range(1, len(arr)):
    if arr[i]*arr[i-1] < 0:
        sign_changes += 1
print(sign_changes)
