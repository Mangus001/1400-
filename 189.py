python

a, b, c, d = int(input()), int(input()), int(input()), int(input())

is_rook_threat = (a == c) or (b == d)

is_bishop_threat = abs(a - c) == abs(b - d)

is_king_reachable = max(abs(a - c), abs(b - d)) == 1

is_queen_threat = (a == c) or (b == d) or (abs(a - c) == abs(b - d))

white_pawn_move = (d == b + 1 and c == a)  
white_pawn_attack = (d == b + 1 and abs(a - c) == 1) 

initial_row = 2
can_move_two_squares = (b == initial_row and d == b + 2 and c == a)

white_pawn_threat = white_pawn_move or white_pawn_attack

black_pawn_move = (d == b - 1 and c == a)
black_pawn_attack = (d == b - 1 and abs(a - c) == 1) 
initial_row_black = 7
can_move_two_squares_b = (b == initial_row_black and d == b - 2 and c == a)

black_pawn_threat = black_pawn_move or black_pawn_attack

knight_moves = [
    (a + 2, b + 1), (a + 2, b - 1),
    (a - 2, b + 1), (a - 2, b - 1),
    (a + 1, b + 2), (a + 1, b - 2),
    (a - 1, b + 2), (a - 1, b - 2)
]
is_knight_threat = (c, d) in knight_moves

print("а) Ладья:", "Да" if is_rook_threat else "Нет")
print("б) Слон:", "Да" if is_bishop_threat else "Нет")
print("в) Король:", "Да" if is_king_reachable else "Нет")
print("г) Ферзь:", "Да" if is_queen_threat else "Нет")
print("д) Пешка белая:", "Да" if white_pawn_threat else "Нет")
print("е) Пешка черная:", "Да" if black_pawn_threat else "Нет")
print("ж) Конь:", "Да" if is_knight_threat else "Нет")
