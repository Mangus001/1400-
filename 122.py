kilometers = float(input())
feet = float(input())

feet_in_meters = feet * 0.3048

kilometers_in_meters = kilometers * 1000

result = "километрах" if kilometers_in_meters < feet_in_meters else "футах"

print(result)
