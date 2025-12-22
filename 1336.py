students = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Лебедев', 'Морозов', 'Новиков', 'Федоров', 'Обухов', 'Романов',
            'Баранов', 'Громов', 'Давидов', 'Егоров', 'Захаров', 'Ильин', 'Карпов', 'Лунин', 'Маслов', 'Никитин', 'Орлов', 'Петровский', 'Рябов', 'Самойлов', 'Тарасов']
import random
heights = random.sample(range(150, 200), 25) 

max_height = max(heights)
min_height = min(heights)
max_idx = heights.index(max_height)
min_idx = heights.index(min_height)
print('Самый высокий:', students[max_idx])
print('Самый низкий:', students[min_idx])

sorted_pairs = sorted(zip(heights, students))
second_highest = sorted_pairs[-2]
print('Второй по высоте (без учета максимума):', second_highest[1])
