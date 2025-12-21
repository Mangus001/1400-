def task1197(heights):
    avg = sum(heights) / len(heights)
    return sum(1 for h in heights if h > avg)
