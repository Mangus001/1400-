def sequence_5_46(k):
    if k == 1:
        return (1, 1)
    elif k == 2:
        return (2, 1)
    else:
        num_prev2, den_prev2 = 1, 1
        num_prev1, den_prev1 = 2, 1
        for _ in range(3, k + 1):
            num_curr = num_prev1 + num_prev2
            den_curr = den_prev1 + den_prev2
            num_prev2, den_prev2 = num_prev1, den_prev1
            num_prev1, den_prev1 = num_curr, den_curr
        return (num_curr, den_curr)

def first_n_terms_5_46(n):
    return [sequence_5_46(k) for k in range(1, n + 1)]

print(first_n_terms_5_46(10))
