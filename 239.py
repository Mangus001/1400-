a, b, c = map(int, input("Введите три различных целых числа: ").split())

max_num = max(a, b, c)
min_num = min(a, b, c)

middle_nums = [a, b, c]
middle_nums.remove(max_num)
middle_nums.remove(min_num)
middle = middle_nums[0]

print("Самое большое:", max_num)
print("Самое маленькое:", min_num)
print("Среднее:", middle)
