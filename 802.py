count_0_100 = {0:0, 1:0}
count_0_1000 = {0:0, 1:0}
for _ in range(100):
    flip = random.randint(0, 1)
    count_0_100[flip] += 1
for _ in range(900):
    flip = random.randint(0, 1)
    count_0_1000[flip] += 1
for _ in range(100):
    flip = random.randint(0, 1)
    count_0_1000[flip] += 1
