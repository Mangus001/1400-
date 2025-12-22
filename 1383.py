def is_power_of_five(n):
    while n > 1:
        if n % 5 != 0:
            return False
        n //= 5
    return n == 1

def count_powers_of_five(numbers):
    return sum(1 for num in numbers if is_power_of_five(num))

numbers = [1, 5, 25, 125, 130]
print("Степеней пятерки в последовательности:", count_powers_of_five(numbers))
