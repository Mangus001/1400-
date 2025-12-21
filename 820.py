a, b, c, d, e, f = (random.randint(1,8) for _ in range(6))
def threaten_rook(a,b,c,d):
    return a==c or b==d
def threaten_queen(a,b,c,d):
    return threaten_rook(a,b,c,d) or threaten_bishop(a,b,c,d)
def threaten_knight(a,b,c,d):
    return (abs(a - c) == 2 and abs(b - d) == 1) or (abs(a - c) == 1 and abs(b - d) == 2)
def threaten_bishop(a,b,c,d):
    return abs(a - c) == abs(b - d)
def threaten_king(a,b,c,d):
    return max(abs(a - c), abs(b - d)) == 1

def can_move_and_not_under_attack(fw, fc, ew, ec, e, f_, threat_func):
    return (abs(fw - e) <= 1 and abs(fc - f_) <= 1 and (e != fw or f_ != fc) and not threat_func(ew, ec, e, f_))

print("Ладья и ладья:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_rook))
print("Ладья и ферзь:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_queen))
print("Ладья и конь:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_knight))
print("Ладья и слон:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_bishop))
print("Ферзь и ферзь:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_queen))
print("Ферзь и ладья:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_rook))
print("Ферзь и конь:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_knight))
print("Ферзь и слон:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_bishop))
print("Конь и конь:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_knight))
print("Конь и ладья:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_rook))
print("Конь и ферзь:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_queen))
print("Конь и слон:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_bishop))
print("Слон и слон:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_bishop))
print("Слон и ферзь:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_queen))
print("Слон и конь:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_knight))
print("Слон и ладья:", can_move_and_not_under_attack(a,b,c,d,e,f,threaten_rook))
print("Король и слон:", max(abs(a - e), abs(b - f)) <= 1)
print("Король и ферзь:", max(abs(a - e), abs(b - f)) <= 1)
print("Король и конь:", max(abs(a - e), abs(b - f)) == 1)
print("Король и ладья:", max(abs(a - e), abs(b - f)) == 1)
