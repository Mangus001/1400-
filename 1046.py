lengths = list(map(int, input().split()))
widths = list(map(int, input().split()))
heights = list(map(int, input().split()))
for l, w, h in zip(lengths, widths, heights):
    print(l*w*h)
volumes = [l*w*h for l, w, h in zip(lengths, widths, heights)]
print(volumes)
