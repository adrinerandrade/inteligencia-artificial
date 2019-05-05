from generator import Generator
from distance import DistanceResolver
from roulette import Roulette
from chromosome import Chromosome

class Population:
    def __init__(self, cities):
        self.population_size = 20
        self.population = []
        self.distance_resolver = DistanceResolver(cities)
        gen = Generator()
        for _ in range(self.population_size):
            self.population.append(gen.generate_random_chromosome())
    
    def get_population(self): 
        return self.population

    def next_generation(self):
        parents = self.select_best_parents()
        newPop = []
        newPop.extend(map(lambda tup: tup[0], parents))
        newPop.extend(self.createChildren(parents))
        self.population = newPop

    # Seleciona a melhor metade da população
    def select_best_parents(self):
        distances = []
        for i in range(len(self.population)):
            chromosome = self.population[i]
            distance = self.distance_resolver.calculate_distance(chromosome)
            distances[i] = (chromosome, distance)
        distances.sort(key=lambda tup: tup[1], reverse=True)
        return distances[0:10]

    def createChildren(self, parents):
        roulette = Roulette(parents)
        children = []
        for _ in range(5):
            parent_1 = roulette.select_parent()
            parent_2 = roulette.select_parent()

            # TODO - Crossover e mutação para gerar os dois filhos
            # children.append(Chromosome(child_1))
            # children.append(Chromosome(child_2))
            
        return children
