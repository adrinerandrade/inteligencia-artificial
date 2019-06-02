class Dataset:
  def __init__(self, selected_dataset):
    self.x = []
    self.y = []
    if selected_dataset == 1:
      self.init_dataset_1()
    elif selected_dataset == 2:
      self.init_dataset_2()
    else :
      self.init_dataset_3()
  
  def get_dataset(self):
    return [self.x, self.y]

  def init_dataset_1(self):
    self.x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
    self.y = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

  def init_dataset_2(self):
    self.x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
    self.y = [9.14, 8.14, 8.47, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
  
  def init_dataset_3(self):
    self.x = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 19]
    self.y = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 5.56, 7.91, 6.89, 12.50]