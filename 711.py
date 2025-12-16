courses = 6
groups = 6
data = [list(map(int, input().split())) for _ in range(courses)]

total_per_course = [sum(row) for row in data]
min_course = total_per_course.index(min(total_per_course)) + 1

min_students = float('inf')
min_course_num = 0
min_group_num = 0
for i in range(courses):
    for j in range(groups):
        if data[i][j] < min_students:
            min_students = data[i][j]
            min_course_num = i + 1
            min_group_num = j + 1

min_group_numbers = [row.index(min(row)) + 1 for row in data]

print("Курс с меньшим всего студентов:", min_course)
print("Самая малочисленная группа и курс:", min_course_num, min_group_num)
print("Номера минимальных групп по каждому курсу:", min_group_numbers)
