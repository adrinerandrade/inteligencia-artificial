
import math
import cv2

"""
    FURB - Bacharelado em Ciências da Computação
    Inteligencia Artifical
    Implementação do Seminário de Visão Computacional

    Adriner Maranho de Andrade
    Fábio Luiz Fischer
    Jorge Guilherme Kohn
"""

class Char:
    def __init__(self, cntr):
        self.contour = cntr
        self.bbox = cv2.boundingRect(self.contour)
        [x, y, w, h] = self.bbox

        self.bbox_x = x
        self.bbox_y = y
        self.bbox_width = w
        self.bbox_height = h
        self.bbox_area = self.bbox_width * self.bbox_height

        self.center_x = (self.bbox_x + self.bbox_x + self.bbox_width) / 2
        self.center_y = (self.bbox_y + self.bbox_y + self.bbox_height) / 2

        self.diagonal_size = math.sqrt((self.bbox_width ** 2) + (self.bbox_height ** 2))
        self.aspect_ratio = float(self.bbox_width) / float(self.bbox_height)

    def is_valid_char(self):
        return self.bbox_area > 80 and self.bbox_width > 2 and self.bbox_height > 8 and 0.25 < self.aspect_ratio < 1.0

    def euclidian_dist(self, other):
        return math.sqrt((abs(self.center_x - other.center_x) ** 2) + (abs(self.center_y - other.center_y) ** 2))

    def angle(self, other):
        adjacent = float(abs(self.center_x - other.center_x))
        opposite = float(abs(self.center_y - other.center_y))
        return (math.atan(opposite / adjacent) if adjacent != 0.0 else 1.5708) * (180.0 / math.pi)
