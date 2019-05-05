from random import randint
from location import Location

# Cria uma matriz de cidades com distancias aleatórias
class Cities:
    def __init__(self):
        self.count = 20
        self.x = []
        self.y = []
        for _ in range(self.count):
            # Distancias entre 0..1
            self.x.append(randint(1, 10000) / 10000)
            self.y.append(randint(1, 10000) / 10000)

    def get_city(self, index):
        return Location(self.x[index], self.y[index])

    def get_cities(self):
        return (self.x, self.y)

    def get_cities_count(self):
        return self.count