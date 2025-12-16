best_time = None
while True:
    t = float(input())
    if best_time is None or t < best_time:
        best_time = t
    cont = input()
    if cont.lower() != 'да':
        break
print(best_time)
