from generator import Generator
from distance import DistanceResolver

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
        distances = []
        for i in range(len(self.population)):
            distances[i] = self.distance_resolver.calculate_distance(self.population[i])

        # Realizar operação de geração de uma nova geração
        print('Realiza a operação de uma nova geração (seleção, mutação, crossover)')


    # def catch_best_parents(self):
    #     bests = [sys.float_info.max for y in range(self.size_x)]
    #     value_line_matrix = 0;
    #     for x in range(len(self.matrix)):
    #         value_line_matrix = 0
    #         for y in range(len(self.matrix[x])):
    #             value_line_matrix += self.matrix[x][y]
    #         bests[x] = value_line_matrix
    #     bests.sort()
    #     self.set_best_line(bests)
        
    # def set_best_line(self, bests):
    #     value_line_matrix = 0;
    #     for best_index in range(len(bests) // 2):
    #         for x in range(len(self.matrix)):
    #             value_line_matrix = 0
    #             for y in range(len(self.matrix[x])):
    #                 value_line_matrix += self.matrix[x][y]
    #             if (value_line_matrix == bests[best_index]):
    #                 self.best_parents[x] = self.matrix[x]
