ef isosceles_trapezoid_perimeter(base1, base2, height):
    side = math.sqrt(((base2 - base1) / 2)**2 + height**2)
    return base1 + base2 + 2 * side

base1 = 10
base2 = 14
height1 = 5
height2 = 6

perimeter1 = isosceles_trapezoid_perimeter(base1, base2, height1)
perimeter2 = isosceles_trapezoid_perimeter(base1, base2, height2)

sum_perimeters = perimeter1 + perimeter2
print("Сумма периметров двух трапеций:", sum_perimeters)
