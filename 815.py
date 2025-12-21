for _ in range(5):
    c1 = random.choice(deck)
    c2 = random.choice(deck)
    res = compare_cards(c1, c2)
    if res > 0:
        winner = "Первый"
    elif res < 0:
        winner = "Второй"
    else:
        winner = "Ничья"
    print(f"{c1[0]} {c1[1]} vs {c2[0]} {c2[1]}: {winner}")
