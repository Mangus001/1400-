def is_in_array(number, array):
    return number in array

def count_matches(array, reference):
    count = 0
    for num in array:
        if is_in_array(num, reference):
            count += 1
    return count

# Пример использования
m1 = [1, 2, 3]
m2 = [4, 5, 6]
m3 = [2, 5, 7]

count_m1 = count_matches(m1, m3)
count_m2 = count_matches(m2, m3)

if count_m1 > count_m2:
    print("В массиве m1 больше чисел, встречающихся в m3")
elif count_m2 > count_m1:
    print("В массиве m2 больше чисел, встречающихся в m3")
else:
    print("Количество совпадений равно")
