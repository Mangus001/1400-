scores = [list(map(int, input().split())) for _ in range(18)]
fives = sum(row.count(5) for row in scores)
trips = [sum(1 for score in row if score == 3) for row in scores]
twos_per_subject = [sum(row[j] == 2 for row in scores) for j in range(3)]
print(fives)
print(trips)
print(twos_per_subject)
