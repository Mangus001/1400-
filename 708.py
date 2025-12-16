data = [list(map(float, input().split())) for _ in range(12)]
for i in range(12):
    max_month_salary = max(data[i])
    print(i+1, data[i].index(max_month_salary)+1)
for j in range(3):
    col = [data[i][j] for i in range(12)]
    max_salary_worker = max(col)
    print(j+1, col.index(max_salary_worker)+1)
