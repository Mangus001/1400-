masses = list(map(float, input().split()))
full_masses = [mass for mass in masses if mass > 100]
rest_masses = [mass for mass in masses if mass <= 100]
avg_full = sum(full_masses)/len(full_masses)
avg_rest = sum(rest_masses)/len(rest_masses)
print(avg_full, avg_rest)
