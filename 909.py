def task1191(masses):
    full_masses = [x for x in masses if x > 100]
    rest_masses = [x for x in masses if x <= 100]
    mean_full = sum(full_masses) / len(full_masses) if full_masses else None
    mean_rest = sum(rest_masses) / len(rest_masses) if rest_masses else None
    return mean_full, mean_rest
