def task1198(prices):
    average = sum(prices) / len(prices)
    return sum(1 for x in prices if x < average)
