temperatures_month = list(map(int, input().split()))
min_temp = min(temperatures_month)
count_days = temperatures_month.count(min_temp)
print(count_days)
