heights = list(map(float, input().split()))
boys = [h for h in heights if h < 0]
girls = [h for h in heights if h >= 0]
avg_boys = sum(boys)/len(boys)
avg_girls = sum(girls)/len(girls)
print(avg_boys > avg_girls + 10)
