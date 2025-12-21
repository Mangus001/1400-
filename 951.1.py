scores = [1, 0, 3, 1, 0]
first_win = scores.index(3)
first_loss = scores.index(0)
print("Win before loss" if first_win < first_loss else "Loss before win")
