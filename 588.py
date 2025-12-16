x = list(map(float, input().split()))
flag=True
for i in range(len(x)-1):
    if x[i]>x[i+1]:
        print(i+1)
        flag=False
        break
if flag:
    print("Последовательность упорядочена по возрастанию")
