import math

def is_in_geometric_progression(m, g, z):
    if g == 0:
        return m == 0
    if z == 1:
        return m == g
    if m % g != 0:
        return False
    ratio = m / g
    k = math.log(ratio, z)
    return abs(k - round(k)) < 1e-9
