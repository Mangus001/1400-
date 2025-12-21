def threat_by_rook(a, b, c, d):
    return a == c or b == d

def threat_by_bishop(a, b, c, d):
    return abs(a - c) == abs(b - d)

def threat_by_king(a, b, c, d):
    return max(abs(a - c), abs(b - d)) == 1

def threat_by_queen(a, b, c, d):
    return threat_by_rook(a, b, c, d) or threat_by_bishop(a, b, c, d)

a, b, c, d = (random.randint(1,8) for _ in range(4))
print(f"Initial: ({a},{b}) -> Target: ({c},{d})")
print(f"Ладья не угрожает: {not threat_by_rook(a,b,c,d)}")
print(f"Слон не угрожает: {not threat_by_bishop(a,b,c,d)}")
print(f"Король может попасть: {threat_by_king(a,b,c,d)}")
print(f"Ферзь не угрожает: {not threat_by_queen(a,b,c,d)}")
