digits = [int(d) for d in number_str]

max_digit = max(digits)
indices_max = [i for i, d in enumerate(digits) if d == max_digit]
pos_max_from_start = [indices_max[0], indices_max[-1]]  
pos_max_from_end = [len(digits) - 1 - indices_max[-1],
                    len(digits) - 1 - indices_max[0]] 
