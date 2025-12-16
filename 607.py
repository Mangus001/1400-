import sys
car_costs = []
motorcycle_costs = []
for _ in range(75):
    cost = float(input())
    if cost > 5000:
        car_costs.append(cost)
    else:
        motorcycle_costs.append(cost)

if car_costs and motorcycle_costs:
    avg_car = sum(car_costs)/len(car_costs)
    avg_motorcycle = sum(motorcycle_costs)/len(motorcycle_costs)
    print(avg_car > 3*avg_motorcycle)
else:
    print("Недостаточно данных")
