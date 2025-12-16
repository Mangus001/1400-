fib = [1, 1]
total_sum = sum(fib)
while fib[-1] <= 1000:
    next_fib = fib[-1] + fib[-2]
    if next_fib > 1000:
        break
    fib.append(next_fib)
    total_sum += next_fib
print(total_sum)
