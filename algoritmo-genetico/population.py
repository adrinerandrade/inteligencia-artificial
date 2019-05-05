from generator import Generator
from distance import DistanceResolver
from roulette import Roulette
from chromosome import Chromosome
from random import randint
from crossover import Crossover
from mutation import Mutation

class Population:
    def __init__(self, cities):
        # Define o tamanho da população
        self.population_size = 20
        # Lista de população
        self.population = []
        # Instancia a classe de distancia
        self.distance_resolver = DistanceResolver(cities)
        # Obtem os genes
        gen = Generator()
        for _ in range(self.population_size):
            # Cria a população inicial
            self.population.append(gen.generate_random_chromosome())
    
    def get_population(self): 
        return self.select_best_parents(20)

    # Cria a proxima geração
    def next_generation(self):
        # Seleciona os melhors pais
        parents = self.select_best_parents(10)
        # Cria a lista de nova população
        newPop = []
        # Mantes os 10 melhores pais anteriores
        newPop.extend(map(lambda tup: tup[0], parents))
        # Crias os filhos com base nos pais
        newPop.extend(self.createChildren(parents))
        self.population = newPop

    # Seleciona a melhor metade da população
    def select_best_parents(self, limit):
        distances = []
        for i in range(len(self.population)):
            chromosome = self.population[i]
            distance = self.distance_resolver.calculate_distance(chromosome)
            distances.append((chromosome, distance))
        distances.sort(key=lambda tup: tup[1])
        return distances[0:limit]

    # Crias os filhos com base na roleta
    def createChildren(self, parents):
        # executa a releta
        roulette = Roulette(parents)
        children = []
        # Cria 10 filhos
        for _ in range(5):
            parent_1 = roulette.select_parent()
            parent_2 = roulette.select_parent()
            new_children = Crossover(parent_1, parent_2).generate_children()
            Mutation(new_children[0]).mutate()
            Mutation(new_children[1]).mutate()
            children.append(new_children[0])
            children.append(new_children[1])
            
        return children
