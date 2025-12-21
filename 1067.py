p = [int(input()) for _ in range(10)]
q = [ (-p[i]) if 2 <= i <= 9 else p[i]* (i+1) for i in range(10)]
