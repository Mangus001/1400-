N = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))

yablok_dostanetsya = k // N
ostatochok = k % N

print(f"Каждому школьнику достанется {yablok_dostanetsya} яблок(а/и).")
print(f"В корзинке останется {ostatochok} яблок(а/и).")
