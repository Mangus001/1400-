def task1179(results):
    wins = sum(1 for x in results if x == 3)
    draws = sum(1 for x in results if x == 1)
    losses = sum(1 for x in results if x == 2)
    return wins, draws, losses
