from random import randint

class Distance:
    def __init__(self):
        self.size_x = 20
        self.size_y = 21
        self.matrix = [[0 for y in range(self.size_y)] for x in range(self.size_x)]
        for x in range(self.size_x):
            for y in range(self.size_y):
                if (x == y - 1):
                    self.matrix[x][y - 1] = 0
                else:
                    value = randint(1, 1000) / 1000
                    self.matrix[x][y - 1] = value
                    self.matrix[y - 1][x] = value

    def duplicate_first_distance(self):
        is_first = True
        first_value = 0;
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                if (is_first):
                    first_value = self.matrix[x][y]
                    is_first = False
            self.matrix[x][self.size_y - 1] = first_value
            is_first = True

    def get_distance(self, x, y):
        return self.matrix[x][y]
