import matplotlib.pyplot as plt
from data_transformer import DataTransformer

class InputError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return rep(self.value)

class Horizon:

  # public methods

  def run(self, x, y, labels, figsize=(20,3), bands=3, colors=("#8BBCD4","#2B7ABD","#0050A0","#EF9483","#E02421", "#A90E0A")): # dark blue, medium blue, light blue, dark red, medium red, light red
    """ Return the entire graph and its plt object

        Look at DataTransformer.transform to see how the data is transformed.

        Keyword arguments:
        x: single array with x values. Distance between neighboring entries have to be the same
        y: two-dimansional array with y values for each entry. 
        labels: array with strings, shown as the labels on the y-axis.
        figsize: (a,b) used when creating the figure (optional)
        bands: default is 3
        colors: array with the colors used for the bands. from dark to light blue, then from dark red to light red.

        Requirements:
        len(y[i]) == len(x) for all 0 <= i < len(y)
        len(y[0]) == len(labels)
        len(colors) == 2*bands

        RETURN: plt object
    """

    self.check_valid_params(x,y,labels,figsize,bands,colors) 
    n = len(y)

    F = self.create_figure(figsize) 
    df = DataTransformer(y, bands)

    for i in range(n):
      ax = F.add_subplot(n, 1, i+1)
      transformed_x, bands = df.transform(y[i], x)

      for idx,band in enumerate(bands):
        ax.fill_between(transformed_x[idx],0,band,color=colors[idx])

      self.adjust_visuals_line(x, df, ax, i, labels)

    return plt

  # private methods
  def create_figure(self, figsize):
    F = plt.figure(figsize=figsize)
    F.clf()
    return F

  def set_theme(self,ax):
    """ hides all ticks and labels on both axes """
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)
    
  def adjust_visuals_line(self, x, df, ax, i, labels):
    """ adjusts the subplot: height, width, labels """
    plt.xlim(0,x[-1])
    plt.ylim(0,df.get_max()/3)
    self.set_theme(ax)
    ax.get_yaxis().set_visible(True)
    ax.set_yticks([])
    ax.set_ylabel(labels[i], rotation="horizontal")
    
  def check_valid_params(self, x,y,labels, figsize, bands, colors):
    """ checks parameters, throws an InputError if parameters are invalid """

    if bands * 2 != len(colors):
      raise InputError("Number of bands invalid for number of colors")

    if len(y) != len(labels):
      raise InputError("Lengths of arrays y and labels are different")

    for i in y:
      if len(x) != len(i):
        raise InputError("Lengths of arrays x and y are different")
