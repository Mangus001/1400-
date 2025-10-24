length = 543
width = 130
side = 130

num_along_length = length // side

num_along_width = width // side
total_squares = num_along_length * num_along_width

print(f"Количество квадратов со стороной {side} мм, которые можно отрезать: {total_squares}")
