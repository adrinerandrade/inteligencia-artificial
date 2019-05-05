from cities import Cities
from population import Population

cities = Cities()
population = Population(cities)

for _ in range(100):
    population.next_generation()

# resultado final
population.get_population()
