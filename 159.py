a = float(input())
b = float(input())
c = float(input())

condition_a = (a < b < c)

condition_b = (b > a > c)

print("a < b < c:", "да" if condition_a else "нет")
print("b > a > c:", "да" if condition_b else "нет")
