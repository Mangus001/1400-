line = input()
desired_length = int(input())
words = line.split()
total_spaces = desired_length - sum(len(w) for w in words)
gaps = len(words) - 1
base = total_spaces // gaps
extra = total_spaces % gaps
result = ''
for i, w in enumerate(words):
    result += w
    if i < gaps:
        result += ' ' * (base + (1 if i < extra else 0))
print(result)
