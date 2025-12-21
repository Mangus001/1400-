lst = [float(input()) for _ in range(int(input()))]
negatives = [i for i, v in enumerate(lst) if v < 0]
if negatives:
    first_neg = negatives[0]
    last_neg = negatives[-1]
    print("Первое отрицательное и все после него")
    print(*lst[first_neg:])
    print("Последнее отрицательное и все слева")
    print(*lst[:last_neg+1])
