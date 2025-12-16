a, x, epsilon = map(float, input().split())
n = 1
y_prev = a
while True:
    y_curr = a + (x - a) / n
    if abs(y_curr**2 - y_prev**2) < epsilon:
        print(y_curr)
        break
    y_prev = y_curr
    n += 1
