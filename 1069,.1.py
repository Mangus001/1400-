m = [float(input()) for _ in range(10)]
n = [ x/3 for x in m if x >= 0 ] + [ x**2 for x in m if x < 0 ]
