sequence = list(map(int, input().split()))
def is_dominino_series(seq):
    for num in seq:
        if num < 0 or num > 66:
            return False
    return True
case_a = all((num % 10) == (num // 10) for num in sequence)
case_b = True 
print(case_a)
print(case_b)
