player1_card = random.choice(deck)
player2_card = random.choice(deck)

rank_order = {rank: i for i, rank in enumerate(ranks)}
suit_order = {suit: i for i, suit in enumerate(suits)}

def compare_cards(c1, c2):
    if suit_order[c1[1]] > suit_order[c2[1]]:
        return 1
    elif suit_order[c1[1]] < suit_order[c2[1]]:
        return -1
    else:
        if rank_order[c1[0]] > rank_order[c2[0]]:
            return 1
        elif rank_order[c1[0]] < rank_order[c2[0]]:
            return -1
        else:
            return 0

result = compare_cards(player1_card, player2_card)
if result > 0:
    winner = "Первый"
elif result < 0:
    winner = "Второй"
else:
    winner = "Ничья"
print(f"Первая карта: {player1_card[0]} {player1_card[1]}")
print(f"Вторая карта: {player2_card[0]} {player2_card[1]}")
print(f"Побеждает: {winner}")
