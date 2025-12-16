def integer_division(b, a):
    count = 0
    while b >= a:
        b -= a
        count += 1
    return count
