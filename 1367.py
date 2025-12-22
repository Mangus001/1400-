def print_line_with_symbols(symbol, count):
    print(symbol * count)

def draw_triangle_ascending():
    for i in range(1, 11):
        print_line_with_symbols('*', i)

def draw_triangle_descending():
    for i in range(10, 0, -1):
        print_line_with_symbols('*', i)
