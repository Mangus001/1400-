m = [int(input()) for _ in range(10)]
n = [ (i+1)*m[i] if i % 2 == 0 else (m[i]/(i+1)) for i in range(10)]
