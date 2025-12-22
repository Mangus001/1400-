def gcd_list(numbers):
    from functools import reduce
    return reduce(gcd, numbers)

numbers = [12, 18, 24, 30]
print(gcd_list(numbers))
