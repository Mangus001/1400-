def task1194(heights):
    boys = [h for h in heights if h < 0]
    girls = [h for h in heights if h > 0]
    mean_boys = sum(boys) / len(boys) if boys else None
    mean_girls = sum(girls) / len(girls) if girls else None
    return mean_boys is not None and mean_girls is not None and (mean_boys - mean_girls) > 10
