n = int(input())
wins_losses = [(int(input()), int(input())) for _ in range(n)]
more_wins = 0
i = 0
while i < n:
    wins, losses = wins_losses[i]
    more_wins += (wins > losses)
    i += 1
