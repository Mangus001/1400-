def trapezoid_perimeter(a, b, h):
    side = math.sqrt(((b - a) / 2) ** 2 + h ** 2)
    return a + b + 2 * side

def trapezoid_area(a, b, h):
    return (a + b) * h / 2
