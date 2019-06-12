class Normalize:
  def __init__(self, train):
    self.min = 0
    self.value_range = 0
    self.calcule(train)

  # obtem o valor minimo, e a diferença 
  def calcule(self, values):
    max = None
    min = None
    for value in values:
      if max == None and min == None:
        min = value
        max = value
      else:
        if max < value:
          max = value
        if min > value:
          min = value
          
    self.value_range = max - min
    self.min = min

  # normaliza os dados com base no valor minimo e diferenca
  def normalize_array(self, array):
    for i in range(len(array)):
      array[i] = (array[i] - self.min) / self.value_range
    return array