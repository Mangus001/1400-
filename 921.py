arr = [random.randint(1, 50) for _ in range(20)]
max_sum = 0
index = 0
for i in range(len(arr)-4):
    s = sum(arr[i:i+5])
    if s > max_sum:
        max_sum = s
        index = i
print(arr[index:index+5])
