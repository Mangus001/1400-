total_div = 0
even_divs = 0
for i in range(1, n + 1):
    if n % i == 0:
        total_div += 1
        if i % 2 == 0:
            even_divs += 1
print(total_div, even_divs)
