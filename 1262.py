num_str = input()
if '.' in num_str:
    integer_part, fractional_part = num_str.split('.',1)
else:
    integer_part, fractional_part = num_str, ''
print(len(integer_part))
print(len(fractional_part))
