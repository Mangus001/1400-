def task1192(heights):
    boys = [h for h in heights if h < 0]
    girls = [h for h in heights if h > 0]
    mean_boys = sum(boys) / len(boys) if boys else None
    mean_girls = sum(girls) / len(girls) if girls else None
    return mean_boys, mean_girls
