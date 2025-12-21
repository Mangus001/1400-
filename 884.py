def task1166(prep):
    even_precip = sum(prep[i] for i in range(1, len(prep)+1) if i % 2 == 0)
    odd_precip = sum(prep[i] for i in range(1, len(prep)+1) if i % 2 != 0)
    return even_precip > odd_precip
