from random import randint

class Distance:
    def __init__(self):
        size = 20
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        for x in range(size):
            for y in range(x, size):
                if (x == y):
                    self.matrix[x][y] = 0
                else:
                    value = randint(1, 1000) / 1000
                    self.matrix[x][y] = value
                    self.matrix[y][x] = value

    def get_distance(self, x, y):
        return self.matrix[x][y]
