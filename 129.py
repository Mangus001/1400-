birth_year = int(input())
birth_month = int(input())
current_year = int(input())
current_month = int(input())

age = current_year - birth_year

if birth_month > current_month:
    age -= 1
elif birth_month == current_month:
    pass 

print(age)
