n = int(input())
digits = [int(d) for d in str(n)][::-1]
arr = [0]*6
arr[:len(digits)] = digits
print(arr)
for d in digits:
    print(d)
