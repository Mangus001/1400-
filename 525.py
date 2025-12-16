children_total = 0
n_classes = 11
children_in_class = [int(input()) for _ in range(n_classes)]
for i in range(0, n_classes, 2):
    children_total += children_in_class[i]
print(children_total)
