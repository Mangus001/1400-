powers = [int(input()) for _ in range(30)]
print("Есть" if any(p > 200 for p in powers) else "Нет")
