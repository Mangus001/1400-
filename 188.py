a3 = int(input())
a2 = int(input())
a1 = int(input())
b2 = int(input())
b1 = int(input())

a = 100 * a3 + 10 * a2 + a1

for a3_candidate in range(1, 10):
    for a2_candidate in range(10):
        for a1_candidate in range(10):
            a_candidate = 100 * a3_candidate + 10 * a2_candidate + a1_candidate
            for b2_candidate in range(1, 10):
                for b1_candidate in range(10):
                    b_candidate = 10 * b2_candidate + b1_candidate
                    s = a_candidate + b_candidate
                    if 100 <= s <= 999:
                        s1 = s // 100
                        s2 = (s // 10) % 10
                        s3 = s % 10
                        print(s1, s2, s3)
