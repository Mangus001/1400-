def sequence_5_43(n):
    a = [1]
    for k in range(1, n + 1):
        a_k = a[-1] * k + 1 / k
        a.append(a_k)
    return a

sequence_5_43(10)  
