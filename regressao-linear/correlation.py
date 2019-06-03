class Correlation:
  def __init__(self, data):
    self.x = data[0]
    self.y = data[1]
    self.mediaX = self.media(self.x)
    self.mediaY = self.media(self.y)

  def calc(self):
    # sem criatividade para nome de variaveis
    val1 = 0
    val2 = 0
    val3 = 0
    for i in range(len(self.x)):
      val1 = val1 + ((self.x[i] - self.mediaX) * (self.y[i] - self.mediaY))
      val2 = val2 + ((self.x[i] - self.mediaX) ** 2)
      val3 = val3 + ((self.y[i] - self.mediaY) ** 2)
    return (val1 / ((val2 * val3) ** (1/2)))

  def media(self, list):
    total_value = 0
    for value in list:
      total_value = total_value + value
    return total_value / len(list)