n = int(input())
a = [int(input()) for _ in range(n)]
first_element = a[0]
count = 0
i = 0
while i < n:
    count += (a[i] == first_element)
    i += 1
