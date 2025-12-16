f1 = lambda x: x**4 + 2*x**3 - x - 1
root1 = bisection_method(f1, 0, 1)

f2 = lambda x: x**3 - 0.2*x**2 - 0.2*x - 1.2
root2 = bisection_method(f2, 1, 1.5)
