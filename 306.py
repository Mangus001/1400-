def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def nth_fibonacci(n):
    if n <= 2:
        return 1
    fib = fibonacci(n)
    return fib[-1]

n = 10
print(f"{n}-й член Фибоначчи: {nth_fibonacci(n)}")
print(f"Первые {n} членов: {fibonacci(n)}")
