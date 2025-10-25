R1 = float(input())
U1 = float(input())
R2 = float(input())
U2 = float(input())

I1 = U1 / R1
I2 = U2 / R2

result = "первому" if I1 < I2 else "второму"

print(result)
