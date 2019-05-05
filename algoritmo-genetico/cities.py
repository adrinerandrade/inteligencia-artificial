from random import randint
from location import Location

class Cities:
    def __init__(self):
        self.count = 20
        self.x = []
        self.y = []
        for i in range(self.count):
            self.x.append(randint(1, 10000) / 10000)
            self.y.append(randint(1, 10000) / 10000)

    def get_city(self, index):
        return Location(self.x[index], self.y[index])