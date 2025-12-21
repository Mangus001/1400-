def task1185(heights):
    count_bigger_170 = sum(1 for h in heights if h > 170)
    can_form_basketball_team = count_bigger_170 >= 5
    return count_bigger_170, can_form_basketball_team
