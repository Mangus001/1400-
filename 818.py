def pawn_move_white(a, b, c, d):
    return (a == c and (b + 1 == d or (b + 1 == d and a != c))) or (abs(a - c) == 1 and b + 1 == d)

def pawn_move_black(a, b, c, d):
    return (a == c and (b - 1 == d or (b - 1 == d and a != c))) or (abs(a - c) == 1 and b - 1 == d)

def knight_threat(a, b, c, d):
    return (abs(a - c) == 2 and abs(b - d) == 1) or (abs(a - c) == 1 and abs(b - d) == 2)

a, b, c, d = (random.randint(1,8) for _ in range(4))
print(f"White pawn move: {pawn_move_white(a,b,c,d)}")
print(f"Black pawn move: {pawn_move_black(a,b,c,d)}")
print(f"Knight threat: {knight_threat(a,b,c,d)}")
