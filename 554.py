n = 20
grades = list(map(int, input().split()))
fives = grades.count(5)
all_have_fives = int(n == grades.count(5))
not_all_have_fives = int(n != grades.count(5))
print(fives * not_all_have_fives + (n if all_have_fives else 0))
