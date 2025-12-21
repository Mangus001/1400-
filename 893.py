def task1175(results):
    wins = sum(1 for x in results if x == 3)
    draws = sum(1 for x in results if x == 1)
    return wins, draws
