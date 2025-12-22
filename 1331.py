states = ['Государство'+str(i+1) for i in range(28)]
population_millions = [50, 120, 75, 60, 80, 55, 90, 70, 65, 85, 95, 40, 110, 100, 130, 45, 35, 125, 150, 105, 95, 115, 85, 125, 70, 60, 80, 100]
area_thousand_km2 = [500, 600, 400, 550, 480, 530, 620, 470, 510, 490, 530, 420, 580, 610, 650, 430, 410, 640, 700, 620, 580, 660, 560, 680, 480, 440, 520, 570]

densities = [population / area for population, area in zip(population_millions, area_thousand_km2)]
min_index = densities.index(min(densities))
print('Страна с минимальной плотностью:', states[min_index])
