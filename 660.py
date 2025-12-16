ages = list(map(int, input().split()))
max_age = ages[0]
min_age = ages[0]
max_pos = 0
min_pos = 0
for i in range(1, len(ages)):
    if ages[i] > max_age:
        max_age = ages[i]
        max_pos = i
    if ages[i] < min_age:
        min_age = ages[i]
        min_pos = i
if max_pos < min_pos:
    print("старший")
else:
    print("младший")
