d = list(map(int, input().split()))
even_nums = [num for num in d if num % 2 == 0]
odd_nums = [num for num in d if num % 2 != 0]

avg_even = sum(even_nums)/len(even_nums) if even_nums else 0
avg_odd = sum(odd_nums)/len(odd_nums) if odd_nums else 0

print(avg_even, avg_odd)
