def check domino_sequence(t1, t2, case=1):
    for i in range(len(t1)):
        left_half = t1[i][0] if case == 1 else t1[i][1]
        right_half = t2[i][1] if case == 1 else t2[i][0]
        if left_half != right_half:
            return i + 1  
    return -1
