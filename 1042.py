import math
import sys
def factorial(n):
    res = [1]
    for i in range(2, n+1):
        carry = 0
        for j in range(len(res)):
            temp = res[j] * i + carry
            res[j] = temp % 10
            carry = temp // 10
        while carry:
            res.append(carry % 10)
            carry //= 10
    return res[::-1]
digits_factorial = factorial(math.factorial(100))
print(digits_factorial)
