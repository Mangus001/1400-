all_bones = [(i, j) for i in range(7) for j in range(i,7)]
bone1 = random.choice(all_bones)
bone2 = random.choice(all_bones)
can_attach = (bone1[1] == bone2[0]) or (bone1[0] == bone2[1])
