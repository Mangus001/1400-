people = [("Иванов", 180, "муж"), ("Петров", 175, "муж"), ("Сидоров", 165, "муж")]
avg_height_men = sum(h for f, h, g in people if g=="муж")/sum(1 for f,h,g in people if g=="муж")
