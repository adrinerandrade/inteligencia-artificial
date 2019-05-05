from cities import Cities
from population import Population
from distance import DistanceResolver
import matplotlib.pyplot as plt
import matplotlib

cities = Cities()
population = Population(cities)

for _ in range(10000):
    population.next_generation()

# resultado final
for chromosome in population.get_population():
    print(chromosome.get_cities())
    print(DistanceResolver(cities).calculate_distance(chromosome))

cmap = matplotlib.cm.flag
cmap.set_bad(color='white')
plt.imshow([[1,1,1], [1,1,1], [1,1,1]], cmap)
plt.show(block=True)
plt.pause(0.1)
plt.clf()