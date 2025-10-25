a = int(input())
b = int(input())

is_a_divisor_b = (b % a == 0)

is_b_divisor_a = (a % b == 0)

print("a является делителем b:", "да" if is_a_divisor_b else "нет")
print("b является делителем a:", "да" if is_b_divisor_a else "нет")
