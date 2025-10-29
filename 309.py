def sequence_5_47(n):
    v = [0, 0, 1.5] 
    for i in range(3, n):
        v.append(v[i - 1] + v[i - 2])
    return v[n - 1]

n = 10
print(f"v{n} = {sequence_5_47(n)}")
