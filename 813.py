ranks = ["6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
suits = ["пика", "трефы", "бубны", "червы"]
deck = [(rank, suit) for suit in suits for rank in ranks]
card = random.choice(deck)
print(f"Выбрана {card[0]} {card[1]}")
