students['1а'] = 25
students['Nовая'] = 30
del students['-old_class']
total_students = sum(students.values())

for cls, count in students.items():
    print(cls, count)
