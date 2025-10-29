initial_area = 100  
initial_yield = 20  
area_growth = 0.05  
yield_increase = 0.02  

yields = [initial_yield]
areas = [initial_area]

for year in range(2, 9):
    new_area = areas[-1] * (1 + area_growth)
    areas.append(new_area)
    
    new_yield = yields[-1] * (1 + yield_increase)
    yields.append(new_yield)

print("Урожайность по годам (ц/га):")
for i in range(1, 8):
    print(f"Год {i+1}: {yields[i]:.2f}")

print("\nПлощадь участков (га):")
for i in range(3, 7):
    print(f"Год {i+1}: {areas[i]:.2f}")

total_harvest = 0
for i in range(6):
    total_harvest += areas[i] * yields[i]
print(f"\nОбщий сбор за первые 6 лет: {total_harvest:.2f} ц")
