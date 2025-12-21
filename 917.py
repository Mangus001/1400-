def task1199(prep):
    average = sum(prep) / len(prep)
    days = [i+1 for i, x in enumerate(prep) if x > average]
    return days
