time1 = (10, 30)
time2 = (11, 15)
def time_in_minutes(t):
    return t[0]*60 + t[1]
print("Первое раньше" if time_in_minutes(time1) < time_in_minutes(time2) else "Второе раньше")
