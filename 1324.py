students = [("Иванов", [5,4,5]), ("Петров", [3,4,4]), ("Сидоров", [5,5,5])]
avg_scores = []
for f, scores in students:
    mean = sum(scores)/len(scores)
    avg_scores.append((f, mean))
overall_mean = sum(mean for _, mean in avg_scores)/len(avg_scores)
for f, mean in avg_scores:
    if mean > overall_mean:
        print(f)
