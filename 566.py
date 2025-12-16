wins=0
draws=0
losses=0
diff_ge3=0
points=0
for _ in range(20):
    ab=input()
    a=int(ab[0])
    b=int(ab[1]) if len(ab)>1 else 0
    if a>b:
        result='выигрыш'
        wins+=1
        points+=3
    elif a==b:
        result='ничья'
        draws+=1
        points+=1
    else:
        result='проигрыш'
        losses+=1
    if abs(a-b)>=3:
        diff_ge3+=1
print(wins, losses, draws, diff_ge3, points)
