from cities import Cities
from population import Population
from distance import DistanceResolver

cities = Cities()
population = Population(cities)

for _ in range(10000):
    population.next_generation()

# resultado final
for chromosome in population.get_population():
    print(chromosome.get_cities())
    print(DistanceResolver(cities).calculate_distance(chromosome))