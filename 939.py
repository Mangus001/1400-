precipitations = [random.uniform(0, 50) for _ in range(31)]
max_precip = max(precipitations)
first_day = precipitations.index(max_precip) + 1
last_day = len(precipitations) - precipitations[::-1].index(max_precip)
print(first_day, last_day)
