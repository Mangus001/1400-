wins_player1 = 0
wins_player2 = 0
draws = 0
for _ in range(100):
    p1 = random.randint(1, 6)
    p2 = random.randint(1, 6)
    if p1 > p2:
        wins_player1 += 1
    elif p2 > p1:
        wins_player2 += 1
    else:
        draws += 1
