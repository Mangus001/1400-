temperatures = list(map(int, input().split()))
min_temp = min(temperatures)
dates = [i+1 for i, t in enumerate(temperatures) if t == min_temp]
print(dates[0], dates[1])
