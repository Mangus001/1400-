python

a, b, c, d, e, f = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())

def threaten_rook(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2

def threaten_bishop(x1, y1, x2, y2):
    return abs(x1 - x2) == abs(y1 - y2)

def threaten_queen(x1, y1, x2, y2):
    return threaten_rook(x1, y1, x2, y2) or threaten_bishop(x1, y1, x2, y2)

def threaten_knight(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

def threaten_king(x1, y1, x2, y2):
    return max(abs(x1 - x2), abs(y1 - y2)) == 1

threaten_by_black = False
threaten_by_black |= threaten_rook(c, d, e, f)
threaten_by_black |= threaten_bishop(c, d, e, f)
threaten_by_black |= threaten_queen(c, d, e, f)
threaten_by_black |= threaten_knight(c, d, e, f)
threaten_by_black |= threaten_king(c, d, e, f)


can_move = False

if a == e or b == f:
    if not threaten_by_black:
        can_move = True

if not threaten_by_black and (threaten_rook(a, b, e, f) or threaten_bishop(a, b, e, f)):
    can_move = True

if not threaten_by_black and threaten_knight(a, b, e, f):
    can_move = True

if not threaten_by_black and threaten_bishop(a, b, e, f):
    can_move = True

if not threaten_by_black and threaten_king(a, b, e, f):
    can_move = True

print("Да" if can_move else "Нет")
