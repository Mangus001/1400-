import math

def hypotenuse(cat1, cat2):
    return math.sqrt(cat1**2 + cat2**2)

def perimeter_ABCD(AB, AD, CD):
    BC = hypotenuse(AB, AD)  
    return AB + AD + CD + hypotenuse(AB, AD)

AB = 3
AD = 4
CD = 5 
print("Периметр ABCD:", perimeter_ABCD(AB, AD, CD))
