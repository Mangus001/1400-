n=20
grades = list(map(int, input().split()))
fives = grades.count(5)
all_fives = int(n==fives)
not_all_fives = int(n!=fives)
print(fives * not_all_fives + (n*all_fives))
