people = [(25, "муж"), (30, "жен"), (40, "муж")]
mass_men = sum(80 for age, gender in people if gender=="муж")
