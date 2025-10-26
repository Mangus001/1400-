number = int(input("Введите натуральное число: "))


n = int(input("Введите количество последних цифр (n): "))


sum_digits = 0
product_digits = 1

for _ in range(n):
    digit = number % 10      
    sum_digits += digit      
    product_digits *= digit  
    number //= 10            

print("Сумма последних n цифр:", sum_digits)
print("Произведение последних n цифр:", product_digits)
