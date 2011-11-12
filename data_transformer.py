import numpy as np

class DataTransformer:

  def __init__(self, all_data, bands):
    self.min = 0
    self.max = 0

    self.num_band = bands
    self.band = 0
    self.set_data(all_data)
  
  # public methods
  def set_data(self, data):
    self.all_data = data
    self.max = max(max(data))
    self.min = min(min(data))

    if abs(self.max ) > abs(self.min):
      self.min = self.max * -1

    if abs(self.max ) < abs(self.min):
      self.max= self.min * -1

    self.band = self.max / self.num_band 
    
  def transform(self, y,x):
    ret = []
    x1 = []
    one_step = x[1] - x[0]

    for i in range(self.num_band*2):
      b = []
      x_new = []

      for idx, y1 in enumerate(y):
        z = 0
        has_crossover = False

        if self.is_still_positive(i): 
          if y1 > 0:
            z = self.calculate_new_y_value(i, y1)
            self.crossover2(idx, x, one_step, b, x_new, y, self.smaller)
            has_crossover, new_x_value = self.crossover(idx, x, one_step,y, self.smaller)
        else:
          if y1 < 0:
            z = self.calculate_new_y_value(i, abs(y1))
            self.crossover2(idx, x, one_step, b, x_new, y, self.larger)
            has_crossover, new_x_value = self.crossover(idx, x, one_step,y, self.larger)

        b.append(z)
        x_new.append(x[idx])
        if has_crossover:
          x_new.append(new_x_value)
          b.append(0)

      ret.append(b)
      x1.append(x_new)

    return x1,ret

  # private methods
  def get_max(self):
    return(self.max)

  def transform_number(self,y1, top, bottom):
    z = 0
    if bottom < y1 and y1 <= top:
      z = y1 - bottom
    elif y1 >= top:
      z = self.band
    return(z)

  def generate_random_x_y(self,y_max=9):
    x = np.arange(0, 2, 0.05)
    y = list(np.random.random_integers(-9,y_max,len(x)))
    return x,y

  def crossover(self, idx, x, one_step, y, m):
    if len(y) > idx + 1 and m(y[idx+1], 0):
        return True,x[idx] + one_step/2.0
    else:
      return False, 0

  def larger(self, a, b):
    return a > b

  def smaller(self, a, b):
    return a < b

  def crossover2(self, idx, x, one_step, b, x_new,y, m):
    if idx > 0 and m(y[idx - 1], 0):
       x_new.append(x[idx] - one_step/2.0)
       b.append(0)

  def is_still_positive(self,i):
    return i < self.num_band
    
  def calculate_new_y_value(self,i,y1):
      top = (i % self.num_band + 1) * self.band
      bottom = (i % self.num_band) * self.band

      return self.transform_number(y1, top , bottom)
