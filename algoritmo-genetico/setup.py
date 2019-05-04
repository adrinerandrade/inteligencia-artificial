from distance import Distance
from fitness import Fitness

distance = Distance()
distance.duplicate_first_distance()
fitness = Fitness(distance.matrix)
fitness.catch_best_parents()
for x in range(len(fitness.best_parents)):
    for y in range(len(fitness.best_parents[x])):
        print(fitness.best_parents[x][y], end = ' ')
    print(' ')
