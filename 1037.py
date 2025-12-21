num1 = [int(d) for d in input().split()]
num2 = [int(d) for d in input().split()]
carry = 0
result_sum = []
for d1, d2 in zip(reversed(num1), reversed(num2)):
    s = d1 + d2 + carry
    result_sum.append(s % 10)
    carry = s // 10
if carry:
    result_sum.append(carry)
result_sum.reverse()
print(*result_sum)

num1 = [int(d) for d in input().split()]
num2 = [int(d) for d in input().split()]
borrow = 0
result_sub = []
for d1, d2 in zip(reversed(num1), reversed(num2)):
    diff = d1 - d2 - borrow
    if diff < 0:
        diff += 10
        borrow = 1
    else:
        borrow = 0
    result_sub.append(diff)
result_sub.reverse()
print(*result_sub)
