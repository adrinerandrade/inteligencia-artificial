import sys

class Fitness:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size_x = 20
        self.size_y = 21
        self.best_parents = [[0 for y in range(self.size_y)] for x in range(self.size_x)]
    
    def catch_best_parents(self):
        bests = [sys.float_info.max for y in range(self.size_x)]
        value_line_matrix = 0;
        for x in range(len(self.matrix)):
            value_line_matrix = 0
            for y in range(len(self.matrix[x])):
                value_line_matrix += self.matrix[x][y]
            bests[x] = value_line_matrix
        bests.sort()
        self.set_best_line(bests)
        
    def set_best_line(self, bests):
        value_line_matrix = 0;
        for best_index in range(len(bests) // 2):
            for x in range(len(self.matrix)):
                value_line_matrix = 0
                for y in range(len(self.matrix[x])):
                    value_line_matrix += self.matrix[x][y]
                if (value_line_matrix == bests[best_index]):
                    self.best_parents[x] = self.matrix[x]