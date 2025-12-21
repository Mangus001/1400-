arr = sorted([random.randint(1, 5) for _ in range(20)])
count_runs = 0
max_run = 0
for i in range(len(arr)):
    if i == 0 or arr[i] != arr[i-1]:
        count_runs += 1
max_run = max((list(map(lambda x: arr.count(x), set(arr)))), default=0)
print(count_runs, max_run
