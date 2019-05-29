import operator
from functools import reduce

class Correlation:

  def __init__(self, x_array, y_array):
    self.x_array = x_array
    self.y_array = y_array

  def calc(self):
    x_average = self.average(self.x_array)
    y_average = self.average(self.y_array)
    

  def average(self, arr):
    sum = reduce(operator.add, arr)
    return sum / len(arr)