def is_even(n):
    return n % 2 == 0

def count_even(seq):
    return sum(1 for n in seq if is_even(n))

def count_odd(seq):
    return sum(1 for n in seq if not is_even(n))

a_sequence = [1, 2, 3, 4, 5, 6, 7, 8]
b_sequence = [10, 11, 12, 13, 14, 15, 16, 17]

print("Четных в первой:", count_even(a_sequence))
print("Нечетных во второй:", count_odd(b_sequence))
