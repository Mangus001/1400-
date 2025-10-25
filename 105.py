k = int(input())

condition1 = (k % 3 == 0)
condition2 = (k % 3 == 1)
condition3 = (k % 3 == 2)

p = (k + 2) // 3
n = 101 + (p - 1) 

digit_index = (k - 1) % 3

digit_str = str(n)
digit_char = digit_str[digit_index]
digit = int(digit_char)

print("k-ая цифра:", digit)
