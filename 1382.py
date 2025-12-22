def is_perfect_square(n):
    return int(math.isqrt(n))**2 == n

def count_squares(numbers):
    return sum(1 for num in numbers if is_perfect_square(num))

numbers = [1, 2, 3, 4, 16, 20]
print("Количество полных квадратов:", count_squares(numbers))
