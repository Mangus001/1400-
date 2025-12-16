count_fives=0
count_fours=0
count_threes=0
count_twos=0
for _ in range(20):
    num=int(input())
    if num>=10:
        s=str(num)
        a=int(s[0])
        b=int(s[1])
    else:
        a=int(s)
        b=0
    if a==5 or b==5:
        count_fives+=1
    if a==4 or b==4:
        count_fours+=1
    if a==3 or b==3:
        count_threes+=1
    if a==2 or b==2:
        count_twos+=1
print(count_fives, count_fours, count_threes, count_twos)
