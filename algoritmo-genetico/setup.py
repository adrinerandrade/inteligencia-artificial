from cities import Cities
from population import Population
from distance import DistanceResolver
import matplotlib.pyplot as plt
import matplotlib

citiesLocation = Cities()
population = Population(citiesLocation)

for _ in range(10000):
    population.next_generation()

# resultado final
final_population = population.get_population()
best_solution = final_population[0]
best_chromosome = best_solution[0]
best_distance = best_solution[1]

plt.plot(citiesLocation.get_cities()[0], citiesLocation.get_cities()[1], 'ro')

best_chromosome_cities = best_chromosome.get_cities()
best_path_x = []
best_path_y = []
for i in range(len(best_chromosome_cities)):
    city = citiesLocation.get_city(best_chromosome_cities[i])
    best_path_x.append(city.x)
    best_path_y.append(city.y)

first_city = citiesLocation.get_city(best_chromosome_cities[0])
best_path_x.append(first_city.x)
best_path_y.append(first_city.y)

plt.plot(best_path_x, best_path_y)

plt.show()
