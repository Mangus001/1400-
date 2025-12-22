students = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Лебедев', 'Морозов', 'Новиков', 'Федоров', 'Обухов', 'Романов',
            'Баранов', 'Громов', 'Давидов', 'Егоров', 'Захаров', 'Ильин', 'Карпов', 'Лунин', 'Маслов', 'Никитин',
            'Орлов', 'Петровский', 'Рябов', 'Самойлов', 'Тарасов']

import random
grades = [[random.randint(2, 5) for _ in range(10)] for _ in range(25)]

sums = [sum(g) for g in grades]

max_idx = sums.index(max(sums))
min_idx = sums.index(min(sums))
print('Фамилия ученика с наибольшей суммой:', students[max_idx])
print('Фамилия ученика с наименьшей суммой:', students[min_idx])
