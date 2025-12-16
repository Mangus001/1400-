total_replacements=0
total_time=0
while True:
    t=int(input())
    if t==0:
        break
    total_replacements+=1
    total_time+=t
print(total_replacements, total_time)
