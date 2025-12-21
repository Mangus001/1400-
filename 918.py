def task11100(grades):
    avg = sum(grades) / len(grades)
    return [i+1 for i, g in enumerate(grades) if g < avg]
