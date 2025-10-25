a, b, c = float(input()), float(input()), float(input())

if (a + b > c) and (a + c > b) and (b + c > a):
    sides = sorted([a, b, c])
    a1, b1, c1 = sides[0], sides[1], sides[2]
    
    sum_squares = a1**2 + b1**2
    c_square = c1**2
    
    if abs(sum_squares - c_square) < 1e-9:
        print("Треугольник прямоугольный")
    elif sum_squares > c_square:
        print("Треугольник остроугольный")
    else:
        print("Треугольник тупоугольный")
    
    if abs(a - b) < 1e-9 and abs(b - c) < 1e-9:
        print("Равносторонний")
    elif abs(a - b) < 1e-9 or abs(b - c) < 1e-9 or abs(a - c) < 1e-9:
        print("Равнобедренный")
    else:
        print("Разносторонний")
else:
    print("Треугольника не существует")
