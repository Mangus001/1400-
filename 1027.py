arr = [int(input()) for _ in range(int(input()))]
pair_found = False
for i in range(len(arr)-1):
    if arr[i] % 2 != 0 and arr[i+1] % 2 != 0:
        print(i+1, i+2)
        pair_found = True
        break
if not pair_found:
    print("Пары соседних нечетных чисел не найдено")
