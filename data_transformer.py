import numpy as np

class DataTransformer:

  def __init__(self, all_data):
    self.min = 0
    self.max = 0

    self.num_band = 3
    self.band = 0
    self.set_data(all_data)
  
  def set_data(self, data):
    self.all_data = data
    self.max = max(max(data))
    self.min = min(min(data))

    if abs(self.max ) > abs(self.min):
      self.min = self.max * -1

    if abs(self.max ) < abs(self.min):
      self.max= self.min * -1

    self.band = self.max / self.num_band 
    print(str(self.band)+":: min: "+str(self.min)+" max:" + str(self.max))

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

  def transform(self, y,x):
    ret = []
    x1 = []
    one_step = x[1] - x[0]

    for i in range(self.num_band*2):
      b = []
      x_neu = []

      for idx, y1 in enumerate(y):
        z = 0
        new_x = False

        if i < self.num_band: # positive values
          if y1 > 0:
            top = self.max - i * self.band
            bottom = self.max - (i+1) * self.band
            z = self.transform_number(y1, top , bottom)
            if y1 == 1:
              print(str(top)+"::"+str(bottom)+"::"+str(z)+"::"+str(y1)+"::"+str(len(b)))

            if idx > 0 and y[idx - 1] < 0:
               x_neu.append(x[idx] - one_step/2.0)
               b.append(0)
            if len(y) > idx + 1:
              if y[idx+1] < 0:
                new_x = True
                new_x_value = x[idx] + one_step/2.0
        else:
          if y1 < 0:
            top = (i-self.num_band+1) * self.band
            bottom = (i-self.num_band) * self.band
            z = self.transform_number(-1 * y1, top, bottom)
            if len(y) > idx + 1 and y[idx+1] > 0:
                new_x = True
                new_x_value = x[idx] + one_step/2.0
            if idx > 0 and y[idx - 1] > 0:
               x_neu.append(x[idx] - one_step/2.0)
               b.append(0)

        b.append(z)
        x_neu.append(x[idx])
        if new_x:
          x_neu.append(new_x_value)
          b.append(0)

      if i < self.num_band:
        ret.append(b)
        x1.append(x_neu)
      else:
        ret.insert(self.num_band,b)
        x1.insert(self.num_band, x_neu)

    ret.reverse()
    x1.reverse()
    #print(ret)
    return x1,ret
