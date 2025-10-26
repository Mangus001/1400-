nums = list(map(float, input("Введите три различных числа: ").split()))
min_num = min(nums)
max_num = max(nums)
middle_nums = [n for n in nums if min_num < n < max_num]
avg_middle = sum(middle_nums) / len(middle_nums)
print("Среднее арифметическое средних чисел:", avg_middle)
